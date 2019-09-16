import functools
import logging
import socket
from typing import Dict, List
from urllib import parse

import click
import requests

import bernhard
from tlwatch import util

logger = logging.getLogger(__name__)


def get_latest_block_number(base_url: str) -> int:
    logger.info(f"Fetch latest block number from '{base_url}'")

    response = requests.get(f"{base_url}/latest-block", timeout=10.0)
    response.raise_for_status()
    latest_block_number = response.json().get("blockNumber")
    if not isinstance(latest_block_number, int):
        raise ValueError("got bad response from /latest-block endpoint")
    return latest_block_number


def watch_auction_backend(base_url: str) -> List[Dict]:
    base_url_parsed = parse.urlparse(base_url)
    base_url_without_credentials = base_url_parsed._replace(
        netloc=base_url_parsed.hostname
    ).geturl()

    metric = -1
    description = ""

    try:
        block_number = get_latest_block_number(base_url)
        state = "ok"
        metric = block_number

    except KeyboardInterrupt:
        raise

    except BaseException as exc:
        state = "error"
        description = (
            f"An error occurred while trying to fetch the latest "
            f"block number from '{base_url_without_credentials}': {exc}"
        )

    logger.info(f"Report to Riemann: {state}, {metric} {description}")

    return [
        {
            "service": base_url_without_credentials,
            "host": socket.gethostname(),
            "state": state,
            "metric": metric,
            "description": description,
            "ttl": 30,
        }
    ]


@click.command()
@click.option("--riemann-host", default="localhost", envvar="RIEMANN_HOST")
@click.option("--riemann-port", default=5555, envvar="RIEMANN_PORT")
@click.option(
    "--base-url", required=True, help="The base URL where the backend is available"
)
def auction_backend(riemann_host, riemann_port, base_url):
    """Monitor auction backend for availability."""
    logging.basicConfig(level=logging.INFO)
    logger.info(f"Version {util.get_version()} starting")
    logger.info(f"Watching '{base_url}' backend for availability")

    util.watch_report_loop(
        lambda: bernhard.Client(riemann_host, riemann_port),
        functools.partial(watch_auction_backend, base_url),
        10,
    )

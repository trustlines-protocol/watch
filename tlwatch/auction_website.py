import functools
import logging
import re
from hashlib import md5
from urllib import parse

import bernhard
import click
import requests
from bs4 import BeautifulSoup

from tlwatch import util

logger = logging.getLogger(__name__)


def calculate_website_source_hash(url: str) -> str:
    """Fetch sources of the website and calculate hash.

    Relevant sources are the HTML page and the JavaScript files. For the
    latter ones, only the first party scripts are of interest, which are
    stored at the `/js` directory. The hash is calculated over the
    concatenation of all relevant sources. Be aware that this depends on
    the order of the script imports. This is considered to be fine,
    since reorder them would also change the HTML source.
    """

    source_list = []
    html = requests.get(url).text
    source_list.append(html)
    soup = BeautifulSoup(html, features="html.parser")
    script_url_list = [
        parse.urljoin(url, script.get("src"))
        for script in soup.findAll("script", attrs={"src": re.compile("^/js")})
    ]

    for script_url in script_url_list:
        script = requests.get(script_url).text
        source_list.append(script)

    source_hash = md5("".join(source_list).encode())
    return source_hash.hexdigest()


def watch_auction_website(url: str, original_hash: str):
    current_hash = calculate_website_source_hash(url)
    state = "ok" if current_hash == original_hash else "error"
    return [{"service": "auction-website.source-hash", "state": state, "ttl": 30}]


@click.command()
@click.option("--url", type=str)
def get_website_hash(url: str):
    source_hash = calculate_website_source_hash(url)
    click.echo(source_hash)


@click.command()
@click.option("--riemann-host", default="localhost", envvar="RIEMANN_HOST")
@click.option("--riemann-port", default=5555, envvar="RIEMANN_PORT")
@click.option("--url")
@click.option("--original-hash")
def auction_website(riemann_host, riemann_port, url, original_hash):
    """Monitor auction website for changed sources."""
    logging.basicConfig(level=logging.INFO)
    logger.info(f"version {util.get_version()} starting")
    logger.info(f"watching {url} sources with original hash {original_hash}")

    util.watch_report_loop(
        lambda: bernhard.Client(riemann_host, riemann_port),
        functools.partial(watch_auction_website, url, original_hash),
        10,
    )

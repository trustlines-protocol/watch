import requests
import logging
import json
import bernhard
import click
import functools
import socket
from tlwatch import util
from urllib.parse import urlparse

logger = logging.getLogger(__name__)


def json_rpc_call(url, method, params=None):
    if params is None:
        params = []

    headers = {"content-type": "application/json"}
    payload = {"method": method, "params": params, "jsonrpc": "2.0", "id": 1}
    response = requests.post(url, data=json.dumps(payload), headers=headers)
    if response.ok:
        return response.json().get("result")


def get_blockNumber(url):
    response = json_rpc_call(url, "eth_blockNumber")
    return util.decode_hex_encoded_number(response)


def get_peerCount(url):
    response = json_rpc_call(url, "net_peerCount")
    return util.decode_hex_encoded_number(response)


def get_syncing(url):
    response = json_rpc_call(url, "eth_syncing")
    return response


def watch_jsonrpc(url, event_host):
    try:
        blockNumber = get_blockNumber(url)
        peerCount = get_peerCount(url)
        syncing = get_syncing(url)
        return [
            {
                "service": "jsonrpc.blocknumber",
                "host": event_host,
                "state": "ok",
                "ttl": 30,
                "metric": blockNumber,
                "attributes": {"url": url},
            },
            {
                "service": "jsonrpc.peercount",
                "host": event_host,
                "state": "ok",
                "ttl": 30,
                "metric": peerCount,
                "attributes": {"url": url},
            },
            {
                "service": "jsonrpc.syncing",
                "host": event_host,
                "state": "syncing" if syncing else "ok",
                "ttl": 30,
                "attributes": {"url": url},
            },
        ]
    except KeyboardInterrupt:
        raise

    except BaseException as e:
        logger.warning("error in watch_etherscan:%s", e)
        return [
            {
                "service": service,
                "host": event_host,
                "state": "error",
                "description": str(e),
                "attributes": {"url": url},
            }
            for service in [
                "jsonrpc.blocknumber",
                "jsonrpc.peercount",
                "jsonrpc.syncing",
            ]
        ]


@click.command()
@click.option("--riemann-host", default="localhost", envvar="RIEMANN_HOST")
@click.option("--riemann-port", default=5555, envvar="RIEMANN_PORT")
@click.option(
    "--url", default="http://localhost:8545", help="URL of JSONRPC server to connect to"
)
@click.option(
    "--event-host-dwim",
    is_flag=True,
    help="use hostname from URL or the local machines name as event host",
)
def jsonrpc(riemann_host, riemann_port, url, event_host_dwim):
    """watch geth/parity for latest block number"""
    logging.basicConfig(level=logging.INFO)
    logger.info("version %s starting", util.get_version())
    logger.info("watching %s", url)
    if event_host_dwim:
        hostname = urlparse(url).hostname
        if hostname in ("localhost", "127.0.0.1"):
            event_host = socket.gethostname()
        else:
            event_host = hostname
    else:
        # Let's stay compatible with what we had before
        event_host = url

    util.watch_report_loop(
        lambda: bernhard.Client(riemann_host, riemann_port),
        functools.partial(watch_jsonrpc, url, event_host),
        10,
    )

import click
import tlwatch.etherscan
import tlwatch.jsonrpc


@click.group()
def cli():
    pass


cli.add_command(tlwatch.etherscan.etherscan)
cli.add_command(tlwatch.jsonrpc.jsonrpc)

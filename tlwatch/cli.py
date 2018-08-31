import click
import tlwatch.etherscan
import tlwatch.jsonrpc
import tlwatch.relay
import tlwatch.psql


@click.group()
def cli():
    pass


cli.add_command(tlwatch.etherscan.etherscan)
cli.add_command(tlwatch.jsonrpc.jsonrpc)
cli.add_command(tlwatch.relay.relay)
cli.add_command(tlwatch.psql.psql)

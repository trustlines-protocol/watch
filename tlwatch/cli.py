import click
import pkg_resources
import tlwatch.etherscan
import tlwatch.jsonrpc
import tlwatch.relay
import tlwatch.psql


def report_version():
    click.echo(pkg_resources.get_distribution("trustlines-watch").version)


@click.group(invoke_without_command=True)
@click.option("--version", help="Prints the version of the software", is_flag=True)
@click.pass_context
def cli(ctx, version):
    if version:
        report_version()
    elif ctx.invoked_subcommand is None:
        click.echo(ctx.get_help())
        ctx.exit()


cli.add_command(tlwatch.etherscan.etherscan)
cli.add_command(tlwatch.jsonrpc.jsonrpc)
cli.add_command(tlwatch.relay.relay)
cli.add_command(tlwatch.psql.psql)

import click
from PyCryptoQuote.pycq import core


@click.group()
def cli():
    pass


cli.add_command(core.new)
cli.add_command(core.last)


if __name__ == "__main__":
    cli()

import click

from gob.repository import Repository

@click.group()
@click.pass_context
def cli(ctx):
    pass

@cli.command()
@click.argument('path', type=click.Path(), default=".")
def init(path):
    Repository.create(path)

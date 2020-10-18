import click


@click.group()
@click.pass_context
def cli(ctx):
    click.echo('I am about to invoke %s' % ctx.invoked_subcommand)

@cli.command()
def sync():
    click.echo('The subcommand')

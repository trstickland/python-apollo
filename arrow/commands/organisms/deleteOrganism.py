import click
from parsec.cli import pass_context, json_loads
from parsec.decorators import bioblend_exception, dict_output

@click.command('deleteOrganism')
@click.argument("organismId")


@pass_context
@bioblend_exception
@dict_output
def cli(ctx, organismId):
    """Warning: Undocumented Method
    """
    return ctx.gi.organisms.deleteOrganism(organismId)

import click
from parsec.cli import pass_context, json_loads
from parsec.decorators import bioblend_exception, dict_output

@click.command('findAllValues')


@pass_context
@bioblend_exception
@dict_output
def cli(ctx):
    """Warning: Undocumented Method
    """
    return ctx.gi.cannedvalues.findAllValues()

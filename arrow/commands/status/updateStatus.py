import click
from arrow.cli import pass_context, json_loads
from arrow.decorators import apollo_exception, dict_output, _arg_split

@click.command('updateStatus')
@click.argument("id_number")
@click.argument("new_value")


@pass_context
@apollo_exception
@dict_output
def cli(ctx, id_number, new_value):
    """TODO: Undocumented

Output:

     ???
        
    """
    return ctx.gi.status.updateStatus(id_number, new_value)

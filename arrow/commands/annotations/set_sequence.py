import click
from arrow.cli import pass_context, json_loads
from arrow.decorators import apollo_exception, None_output, _arg_split

@click.command('set_sequence')
@click.argument("organism", type=str)
@click.argument("sequence", type=str)


@pass_context
@apollo_exception
@None_output
def cli(ctx, organism, sequence):
    """Set the sequence for subsequent requests. Mostly used in client scripts to avoid passing the sequence and organism on every function call.

Output:

     None
        
    """
    return ctx.gi.annotations.set_sequence(organism, sequence)

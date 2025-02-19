import click
from arrow.cli import pass_context, json_loads
from arrow.decorators import custom_exception, dict_output


@click.command('add_organism')
@click.argument("common_name", type=str)
@click.argument("directory", type=str)
@click.option(
    "--blatdb",
    help="Server-side path to 2bit index of the genome for Blat",
    type=str
)
@click.option(
    "--genus",
    help="Genus",
    type=str
)
@click.option(
    "--species",
    help="Species",
    type=str
)
@click.option(
    "--public",
    help="User's email",
    is_flag=True
)
@click.option(
    "--metadata",
    help="JSON formatted arbitrary metadata",
    type=str
)
@pass_context
@custom_exception
@dict_output
def cli(ctx, common_name, directory, blatdb="", genus="", species="", public=False, metadata=""):
    """Add an organism

Output:

    a dictionary with information about the new organism
    """
    return ctx.gi.organisms.add_organism(common_name, directory, blatdb=blatdb, genus=genus, species=species, public=public, metadata=metadata)

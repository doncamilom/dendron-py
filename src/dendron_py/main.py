import click
from .classes import *


@click.command()
@click.argument("patterns",
                type=click.Path(exists=True),
                required=True)
@click.option("--output",
              type=click.Path(exists=False),
              default="dendron-output.out",
              help="Name of the output file.")
@click.option("--method",
              type=click.Choice(["crispy", "relaxed", "all"]),
              default="all",
              help="Method to use. ")
def dendron(patterns, output, method):


    c1, c2 = Dendron(name="a", weight=3), Dendron(name="b", weight=10)

    r1 = Dendron(c1,c2, name="root")
    print("Before canonicalization:")
    print(r1)

    r1.canonicalise()
    print("After canonicalization")
    print(r1)

    print(patterns, output, method)
    return 0

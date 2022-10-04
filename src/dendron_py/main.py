import click


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
    print(patterns, output, method)
    print("Que belleza")
    return 0

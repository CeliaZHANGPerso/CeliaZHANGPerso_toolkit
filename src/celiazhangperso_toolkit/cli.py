import click


@click.command()
@click.option(
    "--name",
    help="The person to greet.",
)
def hello(name: str) -> None:
    """Say hello to NAME."""
    click.echo(f"Hello {name}!")


if __name__ == "__main__":
    hello()

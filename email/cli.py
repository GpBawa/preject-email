import click

@click.command()
def cli():
    click.echo("Hello, World...This is just a test!")

if __name__ == '__main__':
    cli()

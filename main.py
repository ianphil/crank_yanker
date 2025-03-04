import click

@click.command()
@click.option('--name', prompt='Your name', help='The name of the user')
def greet(name):
    """Simple program that greets the user."""
    click.echo(f"Hello, {name}! Welcome to the Cycling Agent.")

if __name__ == '__main__':
    greet()
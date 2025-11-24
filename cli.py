import click
from src import main

@click.group()
def cli():
    pass

@cli.command()
@click.argument('path', type=click.Path(exists=True))
def index(path):
    snippets = main.index_snippets(path)
    click.echo(f"Indexed {len(snippets)} snippets.")

@cli.command()
@click.argument('query')
@click.option('--limit', default=5, help='Max number of results to display')
def search(query, limit):
    results = main.search_snippets(query)
    results = results[:limit]
    if results:
        click.echo(f"Found {len(results)} snippet(s):")
        for i, snippet in enumerate(results, 1):
            click.echo(f"{i}. {snippet}")
    else:
        click.echo("No matching snippets found.")

if __name__ == "__main__":
    cli()

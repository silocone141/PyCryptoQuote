import click
from PyCryptoQuote.utils import cipher, utils


@click.command()
def new():
    """
    Generate new random cryptoquote
    """

    quote_data = utils.get_random_quote()
    quote = quote_data[0]
    author = quote_data[1]
    full_quote = quote + '\n' + f"-- {author}"

    utils.store_quote(full_quote)

    quote_scrambled = '\n' + cipher.scramble_text(full_quote)
    click.echo(quote_scrambled)


@click.command()
@click.option("--all", "-a", is_flag=True)
@click.argument("number", type=int, default=1, required=False)
def last(all, number):
    """
    Return the solution of one or all of the last five puzzles
    """

    if number not in range(1, 6):
        click.echo(
            "Only the last five solutions are stored. Pick a number between "
            "1 and 5"
        )
        quit()

    solutions = utils.get_stored_quotes()

    if not all:
        click.echo('\n' + solutions[number - 1])

    else:
        for j in range(0, 5):
            click.echo('\n' + solutions[j])

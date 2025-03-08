# PyCryptoquote


## About

PyCryptoquote is a CLI program that will provide a random English quote using the [Zen Quotes API](https://zenquotes.io/) that has been passed through a simple substitution cipher. PyCryptoQuote was built using [Click](https://click.palletsprojects.com/en/stable/).


## Installation

Download or clone the repo, enter the directory and execute:

```
# Create a virtual environment in a directory named .venv/
python -m venv .venv

# Activate the virtual environment
source .venv/bin/activate

# Install dependencies
pip install --editable .
```

After this, you can start using the CLI `pycq`. Note: To use this tool again after closing the terminal session, you will need to return the directory that the tool is instaled and execute `source .venv/bin/activate` to use the tool again.


## CLI Overview

```
Usage: pycq [OPTIONS] COMMAND [ARGS]...

Options:
  --help  Show this message and exit.

Commands:
  last  Return the solution of one or all of the last five puzzles
  new   Generate new random cipher
```

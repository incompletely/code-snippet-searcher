# Code Snippet Searcher

A simple CLI tool to index and search code snippets in your local projects using fuzzy search.

## Features

- Recursively scan directories for code files (`.py`, `.js`, `.ts`, `.java`, `.cpp`, `.c`, `.rb`)
- Store snippets in a local SQLite database
- Fuzzy search snippets with ranking
- Simple CLI interface using `click`

## Installation


```bash
git clone https://github.com/your-username/code-snippet-searcher.git
cd code-snippet-searcher
python -m pip install -r requirements.txt

and there might a few bugs or idk so feel free to just fix or anything
import pytest
from src import search

def test_search_snippets():
    snippets = ["print('hello')", "def foo(): pass"]
    results = search.search_snippets("print", snippets)
    assert len(results) == 1
    assert "hello" in results[0]

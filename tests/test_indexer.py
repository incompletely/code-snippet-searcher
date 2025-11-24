import pytest
from src import indexer

def test_index_snippets(tmp_path):
    file = tmp_path / "example.py"
    file.write_text("print('hello')")
    
    result = indexer.index_snippets(tmp_path)
    assert isinstance(result, list)
    assert any("print('hello')" in snippet for snippet in result)

import subprocess
import sys

def test_cli_index(tmp_path):
    result = subprocess.run([sys.executable, "cli.py", "index", str(tmp_path)],
                            capture_output=True, text=True)
    assert "Indexing snippets" in result.stdout

def test_cli_search():
    result = subprocess.run([sys.executable, "cli.py", "search", "test"],
                            capture_output=True, text=True)
    assert "Searching for" in result.stdout

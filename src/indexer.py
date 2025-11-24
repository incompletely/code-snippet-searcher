import os

CODE_EXTENSIONS = {".py", ".js", ".ts", ".java", ".cpp", ".c", ".rb"}

def index_snippets(path):
    """
    Recursively scan a directory and extract code snippets from files.

    Args:
        path (str or Path): directory to scan

    Returns:
        list[str]: list of code snippets (lines of code)
    """
    snippets = []
    for root, _, files in os.walk(path):
        for file in files:
            ext = os.path.splitext(file)[1]
            if ext.lower() in CODE_EXTENSIONS:
                try:
                    with open(os.path.join(root, file), "r", encoding="utf-8") as f:
                        lines = [line.strip() for line in f if line.strip()]
                        snippets.extend(lines)
                except (UnicodeDecodeError, OSError):
                    continue
    return snippets

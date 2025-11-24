import os
from pathlib import Path

def ensure_dir(path):
    """Create a directory if it doesn't exist."""
    Path(path).mkdir(parents=True, exist_ok=True)

def filter_files(files, extensions):
    """Return only files with the given extensions."""
    return [f for f in files if os.path.splitext(f)[1].lower() in extensions]

def read_file_lines(path):
    """Read a file and return non-empty stripped lines."""
    try:
        with open(path, "r", encoding="utf-8") as f:
            return [line.strip() for line in f if line.strip()]
    except (UnicodeDecodeError, OSError):
        return []

def flatten(list_of_lists):
    """Flatten a list of lists into a single list."""
    return [item for sublist in list_of_lists for item in sublist]

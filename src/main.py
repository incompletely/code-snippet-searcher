from src import indexer, search, database

def index_snippets(path):
    """Scan directory for snippets and save them to the database."""
    database.init_db()
    snippets = indexer.index_snippets(path)
    database.save_snippets(snippets)
    return snippets

def search_snippets(query):
    """Load snippets from the database and perform fuzzy search."""
    snippets = database.load_snippets()
    return search.search_snippets(query, snippets)

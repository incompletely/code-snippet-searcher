from fuzzywuzzy import fuzz, process

def search_snippets(query, snippets, limit=5, threshold=60):
    """
    Perform fuzzy search on a list of snippets.

    Args:
        query (str): search term
        snippets (list[str]): list of code snippets
        limit (int): max results to return
        threshold (int): minimum match score (0-100)

    Returns:
        list[str]: matched snippets
    """
    matches = process.extract(query, snippets, scorer=fuzz.partial_ratio, limit=limit)
    return [snippet for snippet, score in matches if score >= threshold]

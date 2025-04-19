from duckduckgo_search import DDGS

def web_search(query):
    results = DDGS().text(query, max_results=1)
    return results[0]['body']

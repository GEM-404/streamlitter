
from serpapi import GoogleSearch
api_key = "8b966943f5a9a59798032cafd77892639d4db7087d79eba488e3389639ffdafd"


def searcher(country: str, query: str, domain: str) -> dict:

    params = {
      "api_key": f"{api_key}",
      "engine": "google",
      "q": f"{query}",
      "location": f"{country}",
      "google_domain": f"{domain}",
      "gl": "us",
      "hl": "en"
    }

    search = GoogleSearch(params)
    results = search.get_dict()

    return results

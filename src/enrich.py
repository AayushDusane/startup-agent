import time
from urllib.parse import urlparse
from googlesearch import search

BAD_DOMAINS = [
    "linkedin.com",
    "crunchbase.com",
    "facebook.com",
    "twitter.com",
    "instagram.com",
    "youtube.com",
    "wikipedia.org",
    "glassdoor.com",
    "indeed.com",
    "wellfound.com",
    "angel.co"
]


def is_valid_website(url):
    try:
        domain = urlparse(url).netloc.lower()
        return not any(bad in domain for bad in BAD_DOMAINS)
    except Exception:
        return False


def google_search_safe(query, max_results=5, delay=3):
    results = []
    try:
        for url in search(query, num_results=max_results):
            time.sleep(delay)  # RATE LIMIT
            if is_valid_website(url):
                results.append(url)
    except Exception:
        pass
    return results


def find_company_website(company):
    if not company:
        return ""

    query = f"{company} startup official website"
    results = google_search_safe(query)

    return results[0] if results else "print('No valid website found')"

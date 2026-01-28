import time
from urllib.parse import urlparse
from googlesearch import search


BAD_LINKEDIN_KEYWORDS = [
    "/company/",
    "/posts/",
    "/jobs/",
    "/learning/",
]


def is_valid_linkedin_profile(url):
    if "linkedin.com/in/" not in url:
        return False

    return not any(bad in url for bad in BAD_LINKEDIN_KEYWORDS)


def find_founder_linkedin(founder_name, company):
    if not founder_name or not company:
        return ""

    query = f"{founder_name} {company} LinkedIn"

    try:
        for url in search(query, num_results=5):
            time.sleep(3)  # rate limit
            if is_valid_linkedin_profile(url):
                return url
    except Exception:
        pass

    return ""

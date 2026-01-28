import requests
from bs4 import BeautifulSoup
import re


FOUNDER_KEYWORDS = [
    "founder",
    "co-founder",
    "ceo",
    "chief executive"
]


def find_founder_from_website(website):
    if not website:
        return ""

    try:
        headers = {"User-Agent": "Mozilla/5.0"}
        res = requests.get(website, headers=headers, timeout=15)
        res.raise_for_status()

        soup = BeautifulSoup(res.text, "lxml")
        text = soup.get_text(" ", strip=True).lower()

        for keyword in FOUNDER_KEYWORDS:
            pattern = rf"{keyword}\s+([A-Z][a-z]+(?:\s+[A-Z][a-z]+)*)"
            match = re.search(pattern, soup.get_text(" ", strip=True))
            if match:
                return match.group(1)

    except Exception:
        pass

    return ""

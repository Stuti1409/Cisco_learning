import requests
from bs4 import BeautifulSoup
import logging

logger = logging.getLogger(__name__)

def fetch_html(url: str, timeout: int = 10) -> str:
    resp = requests.get(url, timeout=timeout)
    resp.raise_for_status()
    return resp.text

def parse_hospital_info_from_html(html: str):
    soup = BeautifulSoup(html, "html.parser")
    data = {"name": None, "departments": [], "address": None}
    # Attempt some common selectors — can be extended
    name_tag = soup.find(["h1", "h2"])
    if name_tag:
        data["name"] = name_tag.get_text(strip=True)
    # departments list heuristics
    dept_candidates = soup.select("ul.departments li, .departments li, #departments li")
    if dept_candidates:
        data["departments"] = [d.get_text(strip=True) for d in dept_candidates]
    # fallback: look for "department" words
    for p in soup.find_all(["p", "div"]):
        text = p.get_text(separator=" ", strip=True)
        if "department" in text.lower() and len(text) < 300:
            data["departments"].append(text)
    # address heuristic
    addr = soup.find(attrs={"class": "address"}) or soup.find("address")
    if addr:
        data["address"] = addr.get_text(strip=True)
    return data

def scrape_hospital(url: str):
    try:
        html = fetch_html(url)
        parsed = parse_hospital_info_from_html(html)
        logger.info("Scraped hospital info", extra={"url": url, "parsed": parsed})
        return parsed
    except Exception as exc:
        logger.exception("Scraping failed for %s: %s", url, exc)
        return {}

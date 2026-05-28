# src/scrapers/naukri.py
from bs4 import BeautifulSoup
from scrapers.base import BaseScraper

class NaukriScraper(BaseScraper):
    def parse_jobs(self, html: str) -> list[dict]:
        soup = BeautifulSoup(html, "html.parser")
        jobs = []
        for card in soup.select(".jobTuple"):  # Naukri job card selector
            title = card.select_one(".title").get_text(strip=True)
            company = card.select_one(".subTitle").get_text(strip=True)
            location = card.select_one(".location").get_text(strip=True) if card.select_one(".location") else None
            jobs.append({
                "title": title,
                "company": company,
                "location": location,
            })
        return jobs

# src/scrapers/base.py
import requests
from abc import ABC, abstractmethod
from sqlalchemy.orm import Session
from db.database import SessionLocal
from db.models import JobPosting

class BaseScraper(ABC):
    def __init__(self):
        self.session: Session = SessionLocal()

    def fetch_html(self, url: str) -> str:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return response.text

    @abstractmethod
    def parse_jobs(self, html: str) -> list[dict]:
        """Extract job postings from HTML. Must be implemented by subclasses."""
        pass

    def save_to_db(self, jobs: list[dict]) -> None:
        for job in jobs:
            posting = JobPosting(**job)
            self.session.add(posting)
        self.session.commit()

    def run(self, url: str) -> None:
        html = self.fetch_html(url)
        jobs = self.parse_jobs(html)
        self.save_to_db(jobs)

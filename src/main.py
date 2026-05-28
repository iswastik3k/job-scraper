# src/main.py
from db.database import engine
from db.models import Base

def init_db():
    Base.metadata.create_all(bind=engine)
    print("Database initialized and tables are ready.")

if __name__ == "__main__":
    init_db()
    
    # src/main.py
    from scrapers.naukri import NaukriScraper

    if __name__ == "__main__":
        scraper = NaukriScraper()
        scraper.run("https://www.naukri.com/data-scientist-jobs")
        print("Scraping complete, jobs saved to DB.")


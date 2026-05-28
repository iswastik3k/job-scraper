# Job Scraper
A Python project for scraping job postings from multiple platforms (LinkedIn, Indeed, Glassdoor, etc.), storing them in a database, and enabling future analytics and dashboards.

## Version 0.1.0

## Features
- Modular scraper architecture with site‑specific implementations
- Database layer (SQLAlchemy + Alembic) for structured storage
- Configurable logging and environment management
- Testing with pytest
- Clean code style enforced with black, flake8, isort

## Project Structure
See `docs/architecture.md` for details.

## Setup
```bash
git clone https://github.com/iswastik3k/job-scraper.git
cd job-scraper
pip install -r requirements.txt
```

## Environment Variables

Copy .env.example to .env and configure:
```Code
DATABASE_URL=postgresql://user:password@localhost:5432/jobs
```

## Testing
```bash
pytest
```
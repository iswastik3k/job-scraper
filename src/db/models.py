# src/db/models.py
from sqlalchemy import Column, Integer, String, Text, DateTime
from sqlalchemy.orm import declarative_base
import datetime

Base = declarative_base()

class JobPosting(Base):
    __tablename__ = "job_postings"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False)
    company = Column(String(255), nullable=False)
    location = Column(String(255))
    salary = Column(String(255))
    description = Column(Text)
    url = Column(String(500), unique=True, nullable=False)
    posted_at = Column(DateTime)
    scraped_at = Column(DateTime, default=datetime.datetime.utcnow)

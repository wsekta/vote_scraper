from abc import ABC, abstractmethod
from src.datatypes import Results

class Scraper(ABC):
  @abstractmethod
  def scrape(self, html: str) -> Results:
    pass
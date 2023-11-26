from src.election import Election
from src.renderer import Renderer
from src.renderer.pyppeteer import Pyppeteer
from src.scraper import Scraper
from src.scraper.bs import BeautifulSoupScraper

class SejmElection(Election):
  def __init__(self,
               year: int = 2023,
               number_of_districts: int = 41,
               renderer: Renderer = Pyppeteer(),
               scraper: Scraper = BeautifulSoupScraper()
              ) -> None:
    if(year == 2023):
      self.global_result_url = "https://wybory.gov.pl/sejmsenat2023/pl/sejm/wynik/pl"
      self.district_result_url = "https://wybory.gov.pl/sejmsenat2023/pl/sejm/wynik/okr"
    self.year = year
    self.number_of_districts = number_of_districts
    self.renderer = renderer
    self.scraper = scraper

  def process_global(self) -> None:
    html = self.renderer.render(self.global_result_url)
    results = self.scraper.scrape(html)
    print(f"WYNIKI GŁOSOWANIA DO SEJMU W ROKU {self.year}:")
    print(results)

  def process_district(self, district_no) -> None:
    html = self.renderer.render(f"{self.district_result_url}/{district_no}")
    results = self.scraper.scrape(html)
    print(f"WYNIKI GŁOSOWANIA DO SEJMU W ROKU {self.year} DLA OKRĘGU {district_no}:")
    print(results)

  def process(self) -> None:
    self.process_global()

    for district_no in range(1, self.number_of_districts + 1):
      self.process_district(district_no)
from src.scraper import Scraper
from src.datatypes import Results, Party
from bs4 import Tag, BeautifulSoup
import re

class BeautifulSoupScraper(Scraper):
  def __init__(self) -> None:
    super().__init__()
    self.parser: BeautifulSoup = None
    self.table: Tag = None
    
  def get_district_name(self, results: Results) -> None:
    for header in self.parser.find_all("h3"):
      if(re.match(".*[oO]kręg [wW]yborczy.*", header.get_text())
         or re.match(".*Polska.*", header.get_text())):
        results.district_name = header.get_text()
        return

  def get_tabel(self) -> None:
    table = self.parser.find_all(id=re.compile("^DataTables_Table_\d+$"))
    self.table: Tag = table[0]

  def parse_result_table(self, results: Results) -> None:
    header_row = self.table.findAll("tr")[0]
    party_name_column = 0
    votes_column = 1
    headers = header_row.findAll("th")
    for idx, column_header in enumerate(headers):
      if("Komitet" == column_header.get_text()
         and headers[party_name_column].get_text() != "Komitet"):
        party_name_column = idx
      if("Liczba głosów" == column_header.get_text()
         and headers[votes_column].get_text() != "Liczba głosów"):
        votes_column = idx

    for row in self.table.findAll("tr")[1:-1]:
      party = Party()
      data = row.findAll("td")
      [name, votes] = data[party_name_column], data[votes_column]
      while len(votes.findAll("div")):
        votes.findAll("div")[0].decompose()
      party.name = name.get_text()
      votes_text = "".join(votes.get_text().split())
      party.votes = int(votes_text)
      results.add_party(party)
  
  def scrape(self, html: str) -> Results:
    results = Results()

    self.parser = BeautifulSoup(html, 'html.parser')

    self.get_tabel()

    self.get_district_name(results)

    self.parse_result_table(results)

    return results
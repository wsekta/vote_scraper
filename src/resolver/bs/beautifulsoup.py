from resolver import Parser
from datatypes import Results, Party
from bs4 import Tag, BeautifulSoup as BS
import re

class BeautifulSoup(Parser):
  def __init__(self) -> None:
    super().__init__()
    self.parser: BS = None
    self.table: Tag = None
    
  def get_district_name(self) -> str:
    for header in self.parser.find_all("h3"):
      if(re.match(".*[oO]kręg [wW]yborczy.*", header.get_text())
         or re.match(".*Polska.*", header.get_text())):
        return header.get_text()

  def get_tabel(self):
    table = self.parser.find_all(id=re.compile("^DataTables_Table_\d+$"))
    self.table: Tag = table[0]

  def parse_result_table(self, results: Results):
    header_row = self.table.findAll("tr")[0]
    party_name_column = 0
    votes_column = 1
    for idx, column_header in enumerate(header_row.findAll("th")):
      if(re.match(".*Komitet.*", column_header.get_text())):
        party_name_column = idx
      if(re.match(".*Liczba głosów.*", column_header.get_text())):
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
  
  def parse(self, html: str) -> Results:
    results = Results()

    self.parser = BS(html, 'html.parser')

    self.get_tabel()

    results.district_name = self.get_district_name()

    self.parse_result_table(results)

    return results
from resolver import Parser
from datatypes import Results, Party
from bs4 import Tag, BeautifulSoup as BS
import re

class BeautifulSoup(Parser):
  def __init__(self) -> None:
    super().__init__()
    self.parser: BS = None
    self.table: Tag = None
    

  def get_tabel(self):
    table = self.parser.find_all(id=re.compile("^DataTables_Table_\d+$"))
    self.table: Tag = table[0]
  
  def parse(self, html: str) -> Results:
    results = Results()
    self.parser = BS(html, 'html.parser')
    self.get_tabel()

    for row in self.table.findAll("tr")[1:-1]:
      party = Party()
      [name, votes] = row.findAll("td")[:2]
      votes.findAll("div")[0].decompose()
      party.name = name.get_text()
      votes_text = "".join(votes.get_text().split())
      party.votes = int(votes_text)
      results.add_party(party)

    return results
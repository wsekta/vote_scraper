from renderer.pyppeteer import Pyppeteer
from resolver.bs import BeautifulSoup

renderer = Pyppeteer()
parser = BeautifulSoup()

# html = renderer.render('https://wybory.gov.pl/sejmsenat2023/pl/sejm/wynik/okr/27')
f = open("resources/page.html", "r")
html = f.read()
results = parser.parse(html)

for party in results.get_parties():
  print(party.name, party.votes)
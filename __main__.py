from src.renderer.pyppeteer import Pyppeteer
from src.scraper.bs import BeautifulSoupScraper

renderer = Pyppeteer()
scraper = BeautifulSoupScraper()

#Poland
#TODO: fix
# html = renderer.render('https://wybory.gov.pl/sejmsenat2023/pl/senat/wynik/pl')
with open("resources/sejm.html") as f:
  html = f.read()

  results = scraper.scrape(html)

  print(results)

# #Senat
# for destrict in range(1,101):
#   html = renderer.render(f'https://wybory.gov.pl/sejmsenat2023/pl/senat/wynik/okr/{destrict}')
#   results = parser.scrape(html)

#   print(results)

# #Sejm
# for destrict in range(1,42):
#   html = renderer.render(f'https://wybory.gov.pl/sejmsenat2023/pl/sejm/wynik/okr/{destrict}')
#   results = parser.scrape(html)

#   print(results)
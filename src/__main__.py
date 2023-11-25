from renderer.pyppeteer import Pyppeteer
from resolver.bs import BeautifulSoup

renderer = Pyppeteer()
parser = BeautifulSoup()

#Poland
#TODO: fix
# html = renderer.render('https://wybory.gov.pl/sejmsenat2023/pl/senat/wynik/pl')
# results = parser.parse(html)

# print(results)

#Senat
for destrict in range(1,101):
  html = renderer.render(f'https://wybory.gov.pl/sejmsenat2023/pl/senat/wynik/okr/{destrict}')
  results = parser.parse(html)

  print(results)

#Sejm
for destrict in range(1,42):
  html = renderer.render(f'https://wybory.gov.pl/sejmsenat2023/pl/sejm/wynik/okr/{destrict}')
  results = parser.parse(html)

  print(results)
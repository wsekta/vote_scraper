from renderer.pyppeteer import Pyppeteer
from parser.bs import BeautifulSoup

renderer = Pyppeteer()
parser = BeautifulSoup()

html = renderer.render('https://wybory.gov.pl/sejmsenat2023/pl/sejm/wynik/okr/27')
results = parser.parse(html)

print(results)
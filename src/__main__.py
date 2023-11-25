from renderer.pyppeteer import Pyppeteer

renderer = Pyppeteer()

print(renderer.render('https://wybory.gov.pl/sejmsenat2023/pl/sejm/wynik/okr/27'))
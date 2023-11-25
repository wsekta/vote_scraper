from bs4 import BeautifulSoup
import re
import asyncio
from pyppeteer import launch

def save_to_file(page):
    f = open("page.html", "w")
    f.write(page)

def get_tab_name(page):
    soup = BeautifulSoup(page, 'html.parser')
    table = soup.findAll(id=re.compile("^DataTables_Table_\d+$"))
    for tab in table:
        print(tab.get('id'))
    return table[0].get('id')

def get_district_page(district_number):
    async def main():
        browserObj = browser = await launch(
                headless=True, 
                args=['--no-sandbox'])
        url = await browserObj.newPage()
        await url.goto(f'https://wybory.gov.pl/sejmsenat2023/pl/sejm/wynik/okr/{district_number}')

        await url.waitForNavigation({"waitUntil": 'networkidle0',})


        ## Get HTML
        htmlContent = await url.content()
        await browserObj.close()
        return htmlContent


    response = asyncio.get_event_loop().run_until_complete(main())
    return response


for district_number in range(1, 42):
    source = get_district_page(district_number)
    table_name = get_tab_name(source)
    print(f"Okręg nr. {district_number} ma tabelę o nazwie: {table_name}")
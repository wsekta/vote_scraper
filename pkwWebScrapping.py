import requests
from bs4 import BeautifulSoup
import re
from requests_html import HTMLSession

def save_to_file(page):
    f = open("page.html", "wb")
    f.write(page)

def get_tab_name(page):
    soup = BeautifulSoup(page, 'html.parser')
    table = soup.findAll(id=re.compile("^DataTables_Table_\d+$"))
    return table[0].get('id')

def get_district_page(district_number):
    page_url = f'https://wybory.gov.pl/sejmsenat2023/pl/sejm/wynik/okr/{district_number}'
    
    try:
        session = HTMLSession()
        response = session.get(page_url)
        return response.html.render()
    except requests.exceptions.RequestException as e:
        print(e)    


district_number = 41
source = get_district_page(district_number)
print(source)
# save_to_file(source)
# table_name = get_tab_name(source)
# print(f"Okręg nr. {district_number} ma tabelę o nazwie: {table_name}")

# districts = []
# for district in range(1, 42):
#     page_url = f'https://wybory.gov.pl/sejmsenat2023/pl/sejm/wynik/okr/{district}'
#     page = requests.get(page_url)
#     soup = BeautifulSoup(page.content, 'html.parser')
    	
#     table = soup.findAll(id=re.compile("^DataTables_Table_\d+"))
#     print(f"Okręg nr. {district} ma {table}")
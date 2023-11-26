from unittest import TestCase
from src.scraper.bs import BeautifulSoupScraper
from src.datatypes import Party

class TestSejmScrapping(TestCase):
  @classmethod
  def setUpClass(cls) -> None:
    scraper = BeautifulSoupScraper()
    with open("resources/sejm.html") as f:
      html = f.read()

    cls.result = scraper.scrape(html)
  
  def test_party_no(self):
    self.assertEqual(len(self.result.parties), 8)
  
  def test_district_name(self):
    self.assertEqual(self.result.district_name, 
                     "sejmowy Okręg wyborczy nr 41")
    
  def test_parties_results(self):
    parties = [
      Party("KOALICYJNY KOMITET WYBORCZY KOALICJA OBYWATELSKA PO .N IPL ZIELONI", 222427),
      Party("KOMITET WYBORCZY PRAWO I SPRAWIEDLIWOŚĆ", 159575),
      Party("KOALICYJNY KOMITET WYBORCZY TRZECIA DROGA POLSKA 2050 SZYMONA HOŁOWNI - POLSKIE STRONNICTWO LUDOWE", 69957),
      Party("KOMITET WYBORCZY NOWA LEWICA", 52032),
      Party("KOMITET WYBORCZY KONFEDERACJA WOLNOŚĆ I NIEPODLEGŁOŚĆ", 32942),
      Party("KOMITET WYBORCZY BEZPARTYJNI SAMORZĄDOWCY", 8985),
      Party("KOMITET WYBORCZY POLSKA JEST JEDNA", 6218),
      Party("KOMITET WYBORCZY WYBORCÓW RUCHU DOBROBYTU I POKOJU", 2172)
    ]

    for partyScraped, partyResult in zip(self.result.parties, parties):
      self.assertEqual(partyScraped.name, partyResult.name)
      self.assertEqual(partyScraped.votes, partyResult.votes)

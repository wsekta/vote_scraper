from unittest import TestCase, mock
from unittest.mock import call, create_autospec
from src.election.sejm import SejmElection
from src.renderer.pyppeteer import Pyppeteer
from src.scraper.bs import BeautifulSoupScraper

class TestSejmElection(TestCase):
  @mock.patch.object(SejmElection, "process_district", autospec=True)
  @mock.patch.object(SejmElection, "process_global", autospec=True)
  def test_process(self, mock_process_global, mock_process_district):
    sejm_election = SejmElection()

    sejm_election.process()

    mock_process_global.assert_called_with(sejm_election)
    expected_process_district_calls = [call(sejm_election, i) for i in range(1, 42)]
    mock_process_district.assert_has_calls(expected_process_district_calls)

  @mock.patch('src.election.sejm.sejm_election.print')
  @mock.patch.object(BeautifulSoupScraper, "scrape", autospec=True)
  @mock.patch.object(Pyppeteer, "render", autospec=True)
  def test_process_district(self, mock_render, mock_scrape, mock_print):
    sejm_election = SejmElection()
    district_no = 3
    mock_render.return_value = "html"
    mock_scrape.return_value = "scraped"

    sejm_election.process_district(district_no)

    mock_render.assert_called_with(sejm_election.renderer, f"{sejm_election.district_result_url}/{district_no}")
    mock_scrape.assert_called_with(sejm_election.scraper, mock_render.return_value)
    expected_print_calls = [call(f"WYNIKI GŁOSOWANIA DO SEJMU W ROKU {sejm_election.year} DLA OKRĘGU {district_no}:"), 
                            call(mock_scrape.return_value)]
    mock_print.assert_has_calls(expected_print_calls)

  @mock.patch('src.election.sejm.sejm_election.print')
  @mock.patch.object(BeautifulSoupScraper, "scrape", autospec=True)
  @mock.patch.object(Pyppeteer, "render", autospec=True)
  def test_process_global(self, mock_render, mock_scrape, mock_print):
    sejm_election = SejmElection()
    district_no = 3
    mock_render.return_value = "html"
    mock_scrape.return_value = "scraped"

    sejm_election.process_global()

    mock_render.assert_called_with(sejm_election.renderer, sejm_election.global_result_url)
    mock_scrape.assert_called_with(sejm_election.scraper, mock_render.return_value)
    expected_print_calls = [call(f"WYNIKI GŁOSOWANIA DO SEJMU W ROKU {sejm_election.year}:"), 
                            call(mock_scrape.return_value)]
    mock_print.assert_has_calls(expected_print_calls)
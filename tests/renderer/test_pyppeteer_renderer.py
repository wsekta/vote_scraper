from unittest import TestCase, mock
from src.renderer.pyppeteer import Pyppeteer
import pytest

class TestPyppeteer(TestCase):
    def setUp(self):
        self.renderer = Pyppeteer()

    @pytest.mark.asyncio
    @mock.patch('src.renderer.pyppeteer.pyppeteer.launch', new_callable=mock.AsyncMock)
    async def test_load(self, mock_launch):
        mock_browser = mock.Mock()
        mock_page = mock.Mock()
        mock_browser.newPage.return_value = mock_page
        mock_launch.return_value = mock_browser

        url = 'https://example.com'
        expected_html_content = '<html><body>Example</body></html>'
        mock_page.content.return_value = expected_html_content

        html_content = await self.renderer.load(url)

        mock_launch.assert_called_once_with(headless=True, args=['--no-sandbox'])
        mock_browser.newPage.assert_called_once()
        mock_page.goto.assert_called_once_with(url)
        mock_page.waitForNavigation.assert_called_once_with({"waitUntil": 'networkidle0', "timeout": 15000})
        mock_page.content.assert_called_once()
        mock_browser.close.assert_called_once()

        self.assertEqual(html_content, expected_html_content)

    @pytest.mark.asyncio
    @mock.patch('src.renderer.pyppeteer.pyppeteer.launch', new_callable=mock.AsyncMock)
    async def test_render(self, mock_launch):
        mock_browser = mock.Mock()
        mock_page = mock.Mock()
        mock_browser.newPage.return_value = mock_page
        mock_launch.return_value = mock_browser

        url = 'https://example.com'
        expected_html_content = '<html><body>Example</body></html>'
        mock_page.content.return_value = expected_html_content

        html_content = await self.renderer.render(url)

        mock_launch.assert_called_once_with(headless=True, args=['--no-sandbox'])
        mock_browser.newPage.assert_called_once()
        mock_page.goto.assert_called_once_with(url)
        mock_page.waitForNavigation.assert_called_once_with({"waitUntil": 'networkidle0', "timeout": 15000})
        mock_page.content.assert_called_once()
        mock_browser.close.assert_called_once()

        self.assertEqual(html_content, expected_html_content)
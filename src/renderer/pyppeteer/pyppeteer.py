import renderer

import asyncio
from pyppeteer import launch

class Pyppeteer(renderer.Renderer):
  async def load(self, url: str) -> str:
    browserObj = browser = await launch(
            headless=True, 
            args=['--no-sandbox'])
    
    page = await browserObj.newPage()

    await page.goto(url)

    await page.waitForNavigation({"waitUntil": 'networkidle0',})

    htmlContent = await page.content()

    await browserObj.close()

    return htmlContent
  

  def render(self, url: str) -> str:
    response = asyncio.get_event_loop().run_until_complete(self.load(url))
    return response
import asyncio
from pyppeteer import launch
import pandas as pd
from urllib.parse import quote

async def html_to_image(url, output_path, selector):
    browser = await launch()
    page = await browser.newPage()
    await page.goto(url)
    element = await page.querySelector(selector)
    bounding_box = await element.boundingBox()
    await page.screenshot({'path': output_path, 'clip': bounding_box})
    await browser.close()
df = pd.read_csv('data/kanji_data.csv') 

base_url = 'http://127.0.0.1:8000/'
selector = '.main' 

for ind in range(len(df)):
    url = base_url + quote(str(ind))
    output_path = f'output/{ind}.png'
    asyncio.get_event_loop().run_until_complete(html_to_image(url, output_path, selector))
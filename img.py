from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pandas as pd
from urllib.parse import quote
import asyncio


df = pd.read_csv('data/kanji_data.csv') 


# Path to your ChromeDriver executable
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--start-maximized')

# Configure ChromeDriver using options
driver = webdriver.Chrome(options=chrome_options)


async def html_to_image(url, output_path):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--start-maximized')

# Configure ChromeDriver using options
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(url)
    driver.execute_script("document.body.style.zoom = '200%'")
    div_element = driver.find_element(By.CSS_SELECTOR, '.main')
    driver.execute_script("arguments[0].scrollIntoView();", div_element)
    screenshot_path = output_path
    driver.save_screenshot(screenshot_path)
    driver.quit()

base_url = 'http://127.0.0.1:8000/'
selector = '.main' 

for ind in range(len(df)):
    url = base_url + quote(str(ind))
    output_path = f'output/{ind}.png'
    asyncio.get_event_loop().run_until_complete(html_to_image(url,output_path))
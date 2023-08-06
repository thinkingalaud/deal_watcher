import requests
from os import environ
from dotenv import load_dotenv
from playwright.sync_api import sync_playwright

load_dotenv()

url = environ['URL']
notification_url = environ['NOTIFICATION_URL']

with sync_playwright() as p:
  browser = p.chromium.launch(headless=False)
  page = browser.new_page()
  page.goto(url)
  page.wait_for_selector('id=selling-essentials')
  selling = page.locator('id=selling-essentials')
  sold_out = "SOLD OUT" in selling.inner_text()
  if !sold_out:
    data = {
      "value1": f"Nordstrom Uppababy Vista back in stock: {url}",
    }
    requests.post(notification_url, json=data, headers={'Content-Type': 'application/json'})
    print("sent notification")

  browser.close()


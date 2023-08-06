import requests
from os import environ
from dotenv import load_dotenv
from playwright.sync_api import sync_playwright

load_dotenv()

url = environ['URL']
notification_url = environ['NOTIFICATION_URL']
css = environ['CSS_SELECTOR']
text = environ['TEXT']
notify_when_contains = environ['NOTIFY_WHEN_CONTAINS'] == 'true'

with sync_playwright() as p:
  browser = p.chromium.launch(headless=False)
  page = browser.new_page()
  page.goto(url)
  page.wait_for_selector(css)
  element = page.locator(css)
  contains = text in element.inner_text()
  if (contains and notify_when_contains) or (not contains and not notify_when_contains):
    data = {
      "value1": f"{url} {'contains' if contains else 'does not contain'} {text}",
    }
    requests.post(notification_url, json=data, headers={'Content-Type': 'application/json'})
    print("sent notification")

  browser.close()


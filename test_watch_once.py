import re
from os import environ
from playwright.sync_api import Page, expect
from dotenv import load_dotenv

load_dotenv()

url = os.environ['URL']
notification_url = os.environ['NOTIFICATION_URL']

def test_watch_one(page: Page):
  print(url)
  print(notification_url)
  page.goto(url)

  # create a locator
  #get_started = page.get_by_role("link", name="Get started")

  

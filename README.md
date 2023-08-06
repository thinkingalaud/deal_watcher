# deal_watcher
Watch webpages for price changes or out of stock changes

# How it works
* playwright-python opens a browser and navigates to your URL
* checks whether the text string does or does not show up in the text of the CSS selector
* hits the notification URL
** IFTTT is used and json with a "value1" is provided, but any webhook that accepts a json payload is fine

# Installation
* install python 3
* `pip install -r requirements.txt`
* write a .env file with the parameters
```
URL=<webpage to watch>
NOTIFICATION_URL=<webhook to hit when condition is satisfied>
CSS_SELECTOR=<css selector for text to watch>
TEXT=<text to search for>
NOTIFY_WHEN_CONTAINS=<boolean, true for a notification when the text is present, false for a notification when the text is NOT present>
```
* set up `python watch_once.py` to run on a recurring basis (cron, etc)


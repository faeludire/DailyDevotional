import re

import requests
from bs4 import BeautifulSoup

website_url_base = 'http://apostolicfaith.org'
website_devotional_url = website_url_base + '/daily-devotional'


def devotional_content_retrieval():
    page = requests.get(website_devotional_url)
    souped = BeautifulSoup(page.text, 'html.parser')

    devotional_url = souped.find_all(class_="article-body")[0].find_all('a', href=True)[0]['href']

    devotional_url = website_url_base + devotional_url

    devotional_conclusion = extract_devotional_conclusion(devotional_url)

    tweet_lines = [devotional_conclusion, devotional_url]
    return tweet_lines


def extract_devotional_conclusion(devotional_url):
    devotional_content = requests.get(devotional_url)
    souped = BeautifulSoup(devotional_content.text, 'html.parser')

    conclusion = souped.find_all("h4")[3].find_next('p')
    conclusion = re.sub("<.*?>", "", str(conclusion)).strip()

    return conclusion

import re

import requests
from bs4 import BeautifulSoup

website_url_base = 'http://apostolicfaith.org'
website_devotional_url = website_url_base + '/daily-devotional'


def devotional_content_retrieval():
    page = requests.get(website_devotional_url)
    souped = BeautifulSoup(page.text, 'html.parser')

    devotional_url = souped.find_all(class_="article-body")[0].find_all('a', href=True)[0]['href']
    sound_cloud_link = souped.find_all("iframe")[0]['src']

    devotional_url = website_url_base + devotional_url

    devotional_conclusion = extract_devotional_details(devotional_url)

    links = devotional_url + '\n' + 'Audio version: ' + sound_cloud_link
    first_tweet = devotional_conclusion[0] + '\n' + links

    tweet_lines = [first_tweet] + devotional_conclusion[1:]

    return tweet_lines


def extract_devotional_details(devotional_url):
    devotional_content = requests.get(devotional_url)
    souped = BeautifulSoup(devotional_content.text, 'html.parser')

    title = souped.find_all('h2')[0]
    title = re.sub("<.*?>", "", str(title)).strip()

    conclusion = souped.find_all(class_="article-content blog")[0].find_all('h4')[0].find_previous_siblings()[0]
    conclusion = re.sub("<.*?>", "", str(conclusion)).strip()

    conclusion1 = souped.find_all("h4")[3].find_next('p')
    conclusion1 = re.sub("<.*?>", "", str(conclusion1)).strip()

    return [title, conclusion, conclusion1]

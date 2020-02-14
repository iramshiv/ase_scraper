import requests
from bs4 import BeautifulSoup
from random import randint
from time import sleep

from src.main.userfunctions.job_scraper import job_scraper

session = requests.Session()  # initializing session variable

# headers set as browsing as from web-browser
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit 537.36 (KHTML, like Gecko) Chrome',
           'Accept': 'text/html,application/xhtml+xml,application/xml; q=0.9,image/webp,*/*;q=0.8'}


def page_number_scraper(url):
    # starting a session with url & header
    req = session.get(url, headers=headers)

    # initializing and parsing with beautifulSoup
    bs = BeautifulSoup(req.text, 'html.parser')

    span_div = bs.find('span', {'class': 'styled__Text-sc-5qktqu-1 hFwQPd'})
    strong_div = span_div.find_all('strong')
    # print(strong_div[1].text)
    return strong_div[1].text


def page_number_first_scraper(url):
    # starting a session with url & header
    req = session.get(url, headers=headers)

    # initializing and parsing with beautifulSoup
    bs = BeautifulSoup(req.text, 'html.parser')

    span_div = bs.find('span', {'class': 'styled__Text-sc-5qktqu-1 hFwQPd'})
    strong_div = span_div.find_all('strong')
    # print(strong_div[1].text)
    # print(url)
    return strong_div[0].text


def page_incrementer(url, duration_value):
    page = {}
    page_number = int(page_number_scraper(url))
    number = 0
    while page_number > 1:
        number = number + 25
        first_url = 'https://www.stepstone.de/5/ergebnisliste.html?stf=freeText&ns=1&companyid=0&sourceofthesearchfield=homepagemex%3Ageneral' \
'&qs=%5B%5D&ke=data%20science&ws=berlin&ra=30&suid=9228097a-4e6f-4450-a66f-2ca1632abeff&ag=age_{}' \
'&of={}&action=paging_next'.format(duration_value, number)
        # print(page_number_first_scraper(first_url))
        page_number -= 1
        # print(first_url)
        sleep(randint(2, 6))
        job_scraper(first_url)
        page[page_number] = {}
        page[page_number]['link'] = first_url
    # print(page)
    return page

# page_number_scraper('https://www.stepstone.de/5/ergebnisliste.html?stf=freeText&ns=1&companyid=0&sourceofthesearchfield=homepagemex%3Ageneral&qs=%5B%5D&ke=data%20science&ws=berlin&ra=30&suid=9228097a-4e6f-4450-a66f-2ca1632abeff&action=facet_selected%3Bage%3Bage_7&ag=age_7')
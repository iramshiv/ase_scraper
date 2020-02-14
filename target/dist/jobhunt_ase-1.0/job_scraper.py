import requests
from bs4 import BeautifulSoup
import time

session = requests.Session()  # initializing session variable

# headers set as browsing as from web-browser
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit 537.36 (KHTML, like Gecko) Chrome',
           'Accept': 'text/html,application/xhtml+xml,application/xml; q=0.9,image/webp,*/*;q=0.8'}


def job_scraper(url):
    jobs_scraped = {}
    # starting a session with url & header
    req = session.get(url, headers=headers)
    time.sleep(2.1)
    # initializing and parsing with beautifulSoup
    bs = BeautifulSoup(req.text, 'html.parser')

    time_div = bs.find_all('li', {'class': 'styled__JobMetadataElement-sc-7an0zf-2 loRBIC'})

    for time_posted in time_div:
        for article_div in bs.find('div', {'class': 'styled__ResultsSectionContainer-gdhf14-0 kOEiOD'}):
            for company_name in article_div.find_all('div', {'class': 'styled__CompanyName-iq4jvn-0 cForES'}):
                for job_link in article_div.find_all('a', {'class': 'styled__TitleLink-sc-7z1cau-0 jJRFLg'}):
                    for job_title in article_div.find_all('h2', {'class': 'styled__TitleWrapper-sc-7z1cau-1 gTbySh'}):

                        title_job = job_title.text
                        jobs_scraped[title_job] = {}
                        print(title_job)

                        company_job = company_name.text
                        jobs_scraped[title_job]['company'] = company_job
                        print(company_job)

                        posted_time_job = time_posted.get_text()
                        jobs_scraped[title_job]['time_posted'] = posted_time_job
                        print(posted_time_job)

                        if 'href' in job_link.attrs:
                            final_link = "https://www.stepstone.de" + job_link.attrs['href']
                            jobs_scraped[title_job]['job_link'] = final_link
                            print(final_link)

                            print("_____-----_____----____")
    # print("Final Data Structure - Dict \n")
    # print(jobs_scraped)

    return jobs_scraped

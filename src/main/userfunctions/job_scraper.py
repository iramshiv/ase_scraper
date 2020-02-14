import requests
from bs4 import BeautifulSoup
from random import randint
from time import sleep

from src.main.userfunctions.save_csv import save_json

session = requests.Session()  # initializing session variable

# headers set as browsing as from web-browser
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit 537.36 (KHTML, like Gecko) Chrome',
           'Accept': 'text/html,application/xhtml+xml,application/xml; q=0.9,image/webp,*/*;q=0.8'}


def job_scraper(url):
    job_list =[]
    jobs = {}

    # starting a session with url & header
    req = session.get(url, headers=headers)

    # initializing and parsing with beautifulSoup
    bs = BeautifulSoup(req.text, 'html.parser')

    article_div = bs.find_all('div', {'class': 'styled__JobItemContentWrapper-sc-11l5pt9-1 ifICmn'})
    time_div = bs.find_all('li', {'class': 'styled__JobMetadataElement-sc-7an0zf-2 loRBIC'})

    for time_posted in time_div:
        # sleep(randint(2, 6))
        for article_div in bs.find('div', {'class': 'styled__ResultsSectionContainer-gdhf14-0 kOEiOD'}):
            # sleep(randint(2, 6))
            for company_name in article_div.find_all('div', {'class': 'styled__CompanyName-iq4jvn-0 cForES'}):
                # sleep(randint(2, 6))
                for job_link in article_div.find_all('a', {'class': 'styled__TitleLink-sc-7z1cau-0 jJRFLg'}):
                    for job_title in article_div.find_all('h2', {'class': 'styled__TitleWrapper-sc-7z1cau-1 gTbySh'}):

                        title_job = job_title.text
                        jobs[title_job] = {}

                        company_job = company_name.text
                        jobs[title_job]['company'] = company_job

                        posted_time_job = time_posted.get_text()
                        jobs[title_job]['time_posted'] = posted_time_job

                        if 'href' in job_link.attrs:
                            final_link = "https://www.stepstone.de" + job_link.attrs['href']
                            jobs[title_job]['job_link'] = final_link
    #job_list.append(jobs)
    #save_json(job_list)
    print(jobs)
    return jobs

#job_scraper('https://www.stepstone.de/5/ergebnisliste.html?stf=freeText&ns=1&companyid=0&sourceofthesearchfield=homepagemex%3Ageneral&qs=%5B%5D&ke=data%20science&ws=berlin&ra=30&suid=9228097a-4e6f-4450-a66f-2ca1632abeff&action=facet_selected%3Bage%3Bage_1&ag=age_1')

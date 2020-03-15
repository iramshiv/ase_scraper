import requests
from bs4 import BeautifulSoup
import csv

session = requests.Session()  # initializing session variable

# headers set as browsing as from web-browser
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit 537.36 (KHTML, like Gecko) Chrome',
           'Accept': 'text/html,application/xhtml+xml,application/xml; q=0.9,image/webp,*/*;q=0.8'}


def tag_scraper(url):
    jobs = {}
    job_number = 1

    try:

        req = session.get(url, headers=headers)
        bs = BeautifulSoup(req.text, 'html.parser')

        # Job Title
        all_div = bs.find_all('div')

        find_job_title_div = all_div[59]
        find_job_title_class = find_job_title_div.attrs['class']
        find_all_job_title = bs.find_all('div', {'class': find_job_title_class})
        for job_title in find_all_job_title:
            # print(job_title.text)
            title = job_title.text
            jobs[job_number] = {}
            jobs[job_number]['job title'] = title

            # Job Link
            all_a = bs.find_all('a')

            find_job_link_div = all_a[59]
            find_job_link_class = find_job_link_div.attrs['class']
            find_all_job_link = bs.find_all('a', {'class': find_job_link_class})
            for job_link in find_all_job_link:
                if 'href' in job_link.attrs:
                    final_link = "https://www.stepstone.de" + job_link.attrs['href']
                    jobs[job_number]['link'] = final_link
                    # print(final_link)

                    # Job Description
                    req_1 = session.get(final_link, headers=headers)
                    bs_1 = BeautifulSoup(req_1.text, 'html.parser')

                    all_div_1 = bs_1.find_all('div')

                    find_job_description_div = all_div_1[70]
                    find_job_description_class = find_job_description_div.attrs['class']
                    find_job_description = bs_1.find_all('div', {'class': find_job_description_class})
                    for job_description in find_job_description:
                        description = job_description.text
                        jobs[job_number]['description'] = description
                        # print(job_description.text)

                    # Company Name
                    find_company_name_div = all_div[60]
                    find_company_name_class = find_company_name_div.attrs['class']
                    find_all_company_name = bs.find_all('div', {'class': find_company_name_class})
                    for company_name in find_all_company_name:
                        name = company_name.text
                        jobs[job_number]['company name'] = name
                        # print(company_name.text)

                    # Posted Time
                    all_ul = bs.find_all('li')

                    find_posted_time_div = all_ul[61]
                    find_posted_time_class = find_posted_time_div.attrs['class']
                    find_all_posted_time = bs.find_all('li', {'class': find_posted_time_class[1]})
                    for posted_time in find_all_posted_time:
                        time_posted = posted_time.get_text()
                        jobs[job_number]['posted time'] = time_posted
                        # print(posted_time.get_text())

                    # Write to CSV
                    with open('jobs.csv', 'w', newline="") as csv_file:
                        writer = csv.writer(csv_file)
                        for key, value in jobs.items():
                            writer.writerow([key, value])

            job_number += 1
            print(job_number)

        # print(jobs)

    except IOError:
        print("I/O error")

    return jobs


tag_scraper(
    'https://www.stepstone.de/5/ergebnisliste.html?stf=freeText&ns=1&qs=%5B%5D&companyID=0&cityID=0&sourceOfTheSearchField=homepagemex%3Ageneral&searchOrigin=Homepage_top-search&ke=data+science&ws=berlin&ra=30&rsearch=1')

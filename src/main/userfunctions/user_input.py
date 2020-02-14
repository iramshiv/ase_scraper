from src.main.userfunctions.duration_check import duration_check
from src.main.userfunctions.job_scraper import job_scraper
from src.main.userfunctions.page_scraper import page_number_scraper, page_number_first_scraper, page_incrementer
from src.main.userfunctions.url_checker import homepage_url_checker, duration_url_checker
from src.main.userfunctions.url_session import session_url
from random import randint
from time import sleep


def main():
    print("Welcome to scraping stepstones.de!!!")

    print("Enter Job Title: (default - Data Science)")
    job_title = input()
    if job_title == "":
        job_title = "data science"

    print("Enter Job Destination: (default - Berlin)")
    job_destination = input()
    if job_destination == "":
        job_destination = "berlin"

    print("Enter Job posted duration: (1- newer than 24 hours, 2- newer than 7 days)")
    job_duration = input()
    duration_value = duration_check(job_duration)
    # print(duration_value)

    # if duration_value == "0":
    # url = homepage_url_checker(job_title, job_destination)
    if duration_value == "1" or duration_value == "2":

        home_url = homepage_url_checker(job_title, job_destination)
        session_url(home_url)
        sleep(randint(2, 6))

        url = duration_url_checker(job_title, job_destination, duration_value)
        # print(url)
    else:
        print("Error!")

    session_code = session_url(url)

    if session_code == 200:
        page_number = int(page_number_scraper(url))
        # print(page_number)
        job_scraper(url)
        if page_number > 0:
            if duration_value == "2":
                duration_value = "7"
                link = page_incrementer(url, duration_value)
            elif duration_value == "1":
                link = page_incrementer(url, duration_value)
        # print(link)

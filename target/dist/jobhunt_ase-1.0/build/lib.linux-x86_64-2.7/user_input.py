from src.unittest.python import duration_check
from src.unittest.python import job_scraper
from src.unittest.python import page_number_scraper, page_incrementer
from src.unittest.python import homepage_url_checker, duration_url_checker
from src.unittest.python import session_url
import time


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

    if duration_value == "1" or duration_value == "2":

        home_url = homepage_url_checker(job_title, job_destination)
        session_url(home_url)

        time.sleep(2.6)

        url = duration_url_checker(job_title, job_destination, duration_check(job_duration))
        session_code = session_url(duration_url_checker(job_title, job_destination, duration_check(job_duration)))

        if session_code == 200:
            page_number = int(page_number_scraper(url))
            job_scraper(url)
            if page_number > 0:
                if duration_value == "2":
                    duration_value = "7"
                    return page_incrementer(url, duration_value)
                elif duration_value == "1":
                    return page_incrementer(url, duration_value)
        else:
            print("Error! URL not available, Please try later")


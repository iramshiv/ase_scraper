from src.main.userfunctions.job_parser import home_job_parser, other_job_parser
from src.main.userfunctions.url_session import session_url
from random import randint
from time import sleep


def homepage_url_checker(url_job, url_city):
    job_parsed = home_job_parser(url_job)
    homepage_url = "https://www.stepstone.de/5/ergebnisliste.html?stf=freeText&ns=1&qs=%5B%5D\
&companyID=0&cityID=0&sourceOfTheSearchField=homepagemex%3Ageneral&searchOrigin=Homepage_top-search\
&ke={}+&ws={}&ra=30".format(job_parsed, url_city)  # Job # City
    # print(homepage_url)
    return homepage_url


def duration_url_checker(day_job, day_city, duration):
    job_parsed = other_job_parser(day_job)

    duration_url = ''

    # session_url(homepage_url_checker(day_job, day_city))
    # sleep(randint(3, 7))

    if duration == "1":
        day = 1
        duration_url = "https://www.stepstone.de/5/ergebnisliste.html?stf=freeText&ns=1\
&companyid=0&sourceofthesearchfield=homepagemex%3Ageneral&qs=%5B%5D\
&ke={}&ws={}&ra=30&suid=9228097a-4e6f-4450-a66f-2ca1632abeff\
&action=facet_selected%3Bage%3Bage_{}&ag=age_{}".format(job_parsed, day_city, day, day)  # Job # City
    elif duration == "2":
        week = 7
        duration_url = "https://www.stepstone.de/5/ergebnisliste.html?stf=freeText&ns=1\
&companyid=0&sourceofthesearchfield=homepagemex%3Ageneral&qs=%5B%5D\
&ke={}&ws={}&ra=30&suid=9228097a-4e6f-4450-a66f-2ca1632abeff\
&action=facet_selected%3Bage%3Bage_{}&ag=age_{}".format(job_parsed, day_city, week, week)  # Job # City
    else:
        print("Invalid Entry")
    # print(duration_url)
    return duration_url

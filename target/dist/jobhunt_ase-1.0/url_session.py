import requests


def session_url(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5)''AppleWebKit 537.36 (KHTML, like Gecko) Chrome',
        'Accept': 'text/html,application/xhtml+xml,application/xml;''q=0.9,image/webp,*/*;q=0.8'}

    if url != "":
        session = requests.Session()
        return session.get(url, headers=headers).status_code


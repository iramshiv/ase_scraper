import requests
import urllib.request
import urllib.error


def session_url(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5)''AppleWebKit 537.36 (KHTML, like Gecko) Chrome',
        'Accept': 'text/html,application/xhtml+xml,application/xml;''q=0.9,image/webp,*/*;q=0.8'}

    while url != "":
        try:
            urllib.request.urlopen(url)
        except urllib.error.HTTPError as e:
            print(e.reason)
            break
        except urllib.error.URLError as e:
            print(e.reason)
            break
        else:
            session = requests.Session()
            request = session.get(url, headers=headers)
            return request.status_code


if __name__ == "__main__":  # pragma: no cover
    import doctest

    doctest.testmod()

    # if request.status_code == 200:
    # return True
    # elif request.status_code != 200:
    # return False
    # print(request.status_code, request.headers, request.text)
    # return request.status_code

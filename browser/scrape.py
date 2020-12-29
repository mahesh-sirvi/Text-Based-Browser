import requests
from bs4 import BeautifulSoup

def browser(url):
    if 'http://' or 'https://' not in url:
        url = 'https://' + url
    r = requests.get(url)

    soup = BeautifulSoup(r.content, 'html.parser')
    find = soup.find_all(['p', 'h', 'a'])
    results = []
    for x in find:
        results.append(x.text)
    return results



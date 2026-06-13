import requests
from bs4 import BeautifulSoup, Comment
import pandas as pd
from io import StringIO
import time

def generate_season_urls():
    urls = []
    url_base = "https://www.hockey-reference.com/leagues/"

    for x in range(2000, 2027):
        if x == 2005:
            continue
        urls.append(f"{url_base}NHL_{x}.html")

    return urls

def extract_season_data(url):
    time.sleep(2)
    print(f"Requesting {int(url.split('_')[1].split('.')[0])}")
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'lxml')

    # Find the commented tables (Team Statistics) and uncomment them
    for comment in soup.find_all(string=lambda text: isinstance(text, Comment)):
        comment.replace_with(BeautifulSoup(comment, 'lxml'))

    stats_table = soup.find('table', {'id': 'stats'})
    if stats_table is None:
        print(f"Table not found")
        return None

    df = pd.read_html(StringIO(str(stats_table)), header=1)[0]

    champion_tag = soup.find('strong', string='League Champion')
    if champion_tag:
        champion = champion_tag.find_next('a').text
    else:
        champion = None

    return df, champion

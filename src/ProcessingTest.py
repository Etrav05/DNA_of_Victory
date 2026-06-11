import pandas as pd
from pathlib import Path

def process(dataframe):
    dataframe = dataframe.rename(columns={'Unnamed: 1': 'Team'})  # Give the teams column a name

    dataframe = dataframe.dropna()  # Drop any N/a records

    # Remove the columns I am not using
    dataframe = dataframe.drop(columns=['Rk', 'GP', 'W', 'L', 'OL', 'SOW', 'SOL', 'SOS',
                                        'PP', 'PPO', 'SHA', 'SO', 'PPOA', 'PIM/G', 'oPIM/G'])
    return dataframe

def generate_season_urls():
    urls = []
    url_base = "https://www.hockey-reference.com/leagues/"

    for x in range(2000, 2027):
        if x == 2005:
            continue
        urls.append(f"{url_base}NHL_{x}.html")

    return urls


if __name__ == '__main__':
    base = Path(__file__).resolve().parent.parent
    file = base / 'data' / 'raw' / '2025-2026_Season.csv'

    df = pd.read_csv(file, header=1)  # Skip the sections row

    df = process(df)

    tables = pd.read_html("https://www.hockey-reference.com/leagues/NHL_2026.html")
    for i, table in enumerate(tables):
        print(f"Table {i}: {table.shape} - {list(table.columns[:18])}")

    #  print(df.to_string())

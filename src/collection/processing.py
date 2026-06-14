import pandas as pd
from pathlib import Path
from src.collection import htmlscrape as htmlsc

cols_to_drop = ['Rk', 'GP', 'W', 'L', 'OL', 'T', 'SOW', 'SOL', 'SOS',
                'PP', 'PPO', 'SHA', 'SO', 'PPOA', 'PIM/G', 'oPIM/G']

def process(dataframe):
    dataframe = dataframe[dataframe['Rk'] != 'Rk']  # Delete the sectioning row

    dataframe = dataframe.rename(columns={'Unnamed: 1': 'Team'})  # Give the teams column a name

    dataframe = dataframe.dropna()  # Drop any N/a records

    # Remove the columns I am not using and that are in the dataframe
    # dataframe = dataframe.drop(columns=[c for c in cols_to_drop if c in dataframe.columns])
    return dataframe


if __name__ == '__main__':
    urls = htmlsc.generate_season_urls()
    tables = []

    for u in urls:
        print("Extraction started...")
        df, champ = htmlsc.extract_season_data(u)  # Gathers team stats and league champion
        print(f'champ: {champ}')

        if df is not None:
            df = process(df)
            year = int(u.split('_')[1].split('.')[0])
            df['Year'] = year
            df['IsChamp'] = (df['Team'] == f'{champ}*')
            tables.append(df)

    combined = pd.concat(tables, ignore_index=True)

    base = Path(__file__).resolve().parent.parent.parent
    combined.to_csv(base / 'data' / 'raw' / 'unaltered_seasons.csv', index=False)
    print("Done processing")

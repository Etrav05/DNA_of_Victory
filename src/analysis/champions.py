import pandas as pd
from pandasql import sqldf
from pathlib import Path

def get_all_champions(df):
    return sqldf("""
        SELECT * FROM
        df WHERE
        IsChamp = 1
    """, locals())

def avg_all_champ_stats(df):
    return df[df['IsChamp'] == 1].mean(numeric_only=True)

if __name__ == '__main__':
    base = Path(__file__).resolve().parent.parent
    df = pd.read_csv(base / 'data' / 'raw' / 'all_seasons.csv')

    # print(get_all_champions(df).to_string())
    avgs = avg_all_champ_stats(df)

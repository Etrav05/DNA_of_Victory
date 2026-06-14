import pandas as pd
from pathlib import Path
import champions as ch


significant_stats = ['S', 'GF', 'PTS', 'PK%', 'SRS', 'AvAge',
                     'GF/G', 'PTS%', 'SV%', 'GA/G', 'PPA', 'GA', 'SA']

# Weight is on a scale fron 1 - 100
weights = { 'S'    : 75,
            'GF'   : 55,
            'PTS'  : 80,
            'PK%'  : 70,
            'SRS'  : 100,
            'AvAge': 40,
            'GF/G' : 55,
            'PTS%' : 85,
            'SV%'  : 75,
            'GA/G' : 95,
            'PPA'  : 80,
            'GA'   : 95,
            'SA'   : 90
}

def Normalize(stat, value, desc):
    mean = desc.loc[desc['Measure'] == 'mean', stat].values[0]
    std = desc.loc[desc['Measure'] == 'std', stat].values[0]
    return (value - mean) / std

def NextNearestNeighbour(all_df, champ_avgs_df, desc, year):
    result_dict = {}
    numeric_stats = champ_avgs.index

    season_df = all_df[all_df['Year'] == year]

    for _, team in season_df.iterrows():
        diff = 0
        for stat in significant_stats:
            diff += abs(Normalize(stat, team[stat], desc) - Normalize(stat, champ_avgs_df[stat], desc)) * weights[stat]
        result_dict[team['Team']] = diff

    result = sorted(result_dict.items(), key=lambda x: x[1])

    return result

def NNN_Every_Year(all_df, champ_avgs_df, desc):
    correct = 0

    for year in range(2000, 2027):
        if year == 2005 or year == 2026:
            continue
        else:
            prediction = NextNearestNeighbour(all_df, champ_avgs_df, desc, year)
            actual = df[(df['Year'] == year) & (df['IsChamp'] == True)]['Team'].values[0]
            print(f"===== {year} ====")
            print(f"Predicted Champion: {prediction[0][0]}")
            print(f"Actual Champion:    {actual}\n")

            if prediction[0][0] == actual:
                correct += 1

    print(f'Correct: {correct}/26')

if __name__ == '__main__':
    base = Path(__file__).resolve().parent.parent.parent
    df = pd.read_csv(base / 'data' / 'raw' / 'all_seasons.csv')
    desc = pd.read_csv(base / 'data' / 'processed' / 'descriptive_stats.csv')

    champ_avgs = ch.avg_all_champ_stats(df)

    # while True:
    #     year = int(input("Enter a year (2000-2025, not 2005): "))
    #
    #     prediction = NextNearestNeighbour(df, champ_avgs, desc, year)
    #     actual = df[(df['Year'] == year) & (df['IsChamp'] == True)]['Team'].values[0]
    #
    #     print(f"\nPredicted Champion: {prediction[0][0]}")
    #     print(f"Actual Champion:    {actual}")
    #     print()
    #     for team, score in prediction[:5]:
    #         print(f"{team}: {score:.2f}")
    #     print()
    #
    NNN_Every_Year(df, champ_avgs, desc)

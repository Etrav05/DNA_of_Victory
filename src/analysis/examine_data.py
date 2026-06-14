import pandas as pd
from pathlib import Path
import champions as ch
from scipy import stats

stats_to_test = ['S', 'GF', 'PTS', 'PK%', 'SH', 'PP%', 'SRS', 'AvAge',
                 'GF/G', 'S%', 'PTS%', 'SV%', 'GA/G', 'PPA', 'GA', 'SA']
def t_test_champion(df):
    for stat in stats_to_test:
        champ_vals = df[df['IsChamp'] == True][stat]
        non_champ_vals = df[df['IsChamp'] == False][stat]
        t, p = stats.ttest_ind(champ_vals, non_champ_vals)
        print(f"{stat}: p-value = {p:.9f}  --- {'Significant' if p < 0.05 else 'Not'}")

if __name__ == '__main__':
    base = Path(__file__).resolve().parent.parent.parent
    df = pd.read_csv(base / 'data' / 'raw' / 'all_seasons.csv')

    # ## Create a file of the descriptive data of this dataset
    # df.describe().to_csv(base / 'data' / 'processed' / 'descriptive_stats.csv')
    #
    # ## Compare champion stats with all other teams and determine the difference
    # champs = df[df['IsChamp'] == True]
    # non_champs = df[df['IsChamp'] == False]
    #
    # comparison = pd.DataFrame({
    #     'Champion Avg': champs.mean(numeric_only=True),
    #     'Non-Champion Avg': non_champs.mean(numeric_only=True),
    #     'Difference': champs.mean(numeric_only=True) - non_champs.mean(numeric_only=True)
    # })
    #
    # base = Path(__file__).resolve().parent.parent
    # comparison.to_csv(base / 'data' / 'processed' / 'champion_comparison.csv')

    t_test_champion(df)

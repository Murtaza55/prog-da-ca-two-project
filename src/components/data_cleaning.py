import pandas as pd

df = pd.read_csv('cricket_test_matches_records_data.csv')

print(df)

df = df.rename(columns={'Mat': 'Matches', 'NO': 'Not_Outs', 'HS': 'Highest_Score', 'Ave': 'Batting_Average', 'BF': 'Balls_Faced', 'SR': 'Strike Rate', '100': '100s', '50': '50s', '0': '0s', '4s': '4s'})

print(df.head())
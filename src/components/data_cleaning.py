import pandas as pd

df = pd.read_csv('cricket_test_matches_records_data.csv')

print(df)

#renaming column names from abreviations to full names
df = df.rename(columns={'Mat': 'Matches', 'NO': 'Not_Outs', 'HS': 'Highest_Score', 'Ave': 'Batting_Average', 'BF': 'Balls_Faced', 'SR': 'Strike_Rate', '100': '100s', '50': '50s', '0': '0s', '4s': '4s'})

# print(df.head())

#finding null data if any
# print(df.isnull().any())

#Getting true for Balls_Faced and Strike rate, checking rows that have null values in those columns
# print(df[df['Balls_Faced'].isna()==1])

#replacing Na value with 0
df['Balls_Faced'] = df['Balls_Faced'].fillna(0)
df['Strike_Rate'] = df['Strike_Rate'].fillna(0)

# print(df[df['Player'] == 'CL Walcott (WI)'])

#Now finding duplicates

#returns true for some rows
print(df.duplicated())

#finding which rows are duplicated, returns 6 rows
print(df[df['Player'].duplicated() == 1])
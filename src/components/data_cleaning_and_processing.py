import pandas as pd
import csv

df = pd.read_csv('cricket_test_matches_records_data.csv')

# print(df)

#=====renaming column names from abreviations to full names=========
df = df.rename(columns={'Mat': 'Matches', 'NO': 'Not_Outs', 'HS': 'Highest_Score', 'Ave': 'Batting_Average', 'BF': 'Balls_Faced', 'SR': 'Strike_Rate', '100': '100s', '50': '50s', '0': '0s', '4s': '4s'})

# print(df.head())

#====finding null data if any========

# print(df.isnull().any())

#Getting true for Balls_Faced and Strike rate, checking rows that have null values in those columns
# print(df[df['Balls_Faced'].isna()==1])

#replacing Na value with 0
df['Balls_Faced'] = df['Balls_Faced'].fillna(0)
df['Strike_Rate'] = df['Strike_Rate'].fillna(0)

# print(df[df['Player'] == 'CL Walcott (WI)'])

#======Now finding duplicates=========

#returns true for some rows
# print(df.duplicated())

#finding which rows are duplicated, returns 6 rows
# print(df[df['Player'].duplicated() == 1])

#dropping duplicates
df = df.drop_duplicates()

#now getting false for all
# print(df.duplicated())

#now getting empty index, no more duplicates
# print(df[df['Player'].duplicated() == 1])

#=====splitting span column to Start Date and End Date=====
splitted_col = df['Span'].str.split(pat = '-')

# print(splitted_col)

# creating columns Start_Year and End_Year to
df['Start_Year'] = df['Span'].str.split(pat = '-').str[0]
df['Final_Year'] = df['Span'].str.split(pat = '-').str[1]

df = df.drop(['Span'], axis=1)

#=======splitting the player name and country from player column=======

# country_with_player = df['Player'].str.split(pat = ')').str[0]

# country_without_player = df['Player'].str.split(pat = '(').str[1]

#removing the circle bracket at the end
df['Country'] = df['Player'].str.split(pat = '(').str[1]

#saving only the country in a seperate columns
df['Country'] = df['Country'].str.split(pat = ')').str[0]

# print(df['Country'])

#Separating player name from country code
df['Player'] = df['Player'].str.split(pat = '(').str[0]

# print(df['Player'])

#====Working on correcting the data types

# print(df.dtypes)

#=====removing * and + from the Highest_Score and Balls Faced and all========

# removing * from Highest_Score column rows
df['Highest_Score'] = df['Highest_Score'].str.split(pat = '*').str[0]

# removing * from Balls_Faced column rows
df['Balls_Faced'] = df['Balls_Faced'].str.split(pat = '+').str[0]

# removing * from Balls_Faced column rows
df['4s'] = df['4s'].str.split(pat = '+').str[0]
df['6s'] = df['6s'].str.split(pat = '+').str[0]

#=====converting datatypes of columns from object to appropriate======

df['Highest_Score'] = df['Highest_Score'].astype(int)

#replacing more null data
df['Balls_Faced'] = df['Balls_Faced'].fillna(0)
# print(df.isnull().any())

df['Balls_Faced'] = df['Balls_Faced'].astype(int)

# print(df.dtypes)

#changing multiple datatypes at once
df = df.astype({'4s':'int', '6s':'int','Start_Year':'int', 'Final_Year':'int'})

# print(df.dtypes)

 # saving the cleaned data in a csv file
df.to_csv('cleaned_test_records_data.csv', index=False)

print("Data saved to", 'cleaned_test_records_data.csv')

#====Calculating each players career length and add it as a new column=====
df['Career_Length'] = df['Final_Year'] - df['Start_Year']

# print(df['Career_Length'])

#====Calculations with the dataframe after adding new columns=====

#Average career length of players

df['Career_Length'].mean()

#Average batting strike rate for players who played more than 10 years

df[df['Career_Length'] > 10]['Strike_Rate'].mean()

#Players who played before 2000
df[df['Start_Year'] < 2000]['Player'].count()

#Players who played after 2000
df[df['Start_Year'] > 2000]['Player'].count()

#Players with the highest score group by country in test innings
testing = df.groupby('Country')['Highest_Score'].max().to_frame('High Scorer')

#Top 10 players with the highest score in an innings in tests

# Returns with all columns
top_10_highest_scores = df.nlargest(10, 'Highest_Score')

# Returns with only two mentioned columns
top_10_highest_scores = df.nlargest(10, 'Highest_Score')[['Player', 'Highest_Score']]

#print(top_10_highest_scores)


# print(df.head())
# Programming for Data Analysis CA-Two Project

 To design and develop a Data Acquisition and Preprocessing Pipeline for CA Two Programming for Data Analysis Course

## *Project Documentation*

## Setting up the project

- Creating Setup.py file to install the packages.
- Creating requirements.txt to list down all the required packages and install them all at once.
- Structuring the project, creating src folder for development.

## Web Scraping

- Worked on web scraping the Cricket Test Matches Records from ESPN Cric info website.
- Using the BeautifulSoup class from bs4 lib parsed the html from the page of the url, first targetted the table to retrieve the data using inspect elements, then targetted the table using the class and found the whole table.
- Extracted the header by targetting the thead of the table and parsed through tr, divs and then each span to get the column names.
- Found all the rows in the table body using tbody, tr and td elements to get the actual rows of data from the table.
- Created a dictionary mapping column names to row values.
- Finally, appending all the data to the list.
- Lastly, saving the scraped data to the csv file using csv module and csv.DictWriter class from python3.

## Data Cleaning

- Worked on cleaning the Cricket Test Matches Records Raw Data after web scraping the data from ESPN Cric Info website.
- Renamed the column names from abreviations to full names, to get full context of each features
- Looked for the null data or any NaN values in rows and replaced them with 0 so it won't create problems later while processing the data.
- Looked for duplicate records and dropped the rows of players that had more than one similar records.
- Removed * and + or any other special characters or rubbish data from the data.
- After cleaning the data, changed and converted columns' data types from object to an appropriate one.
- Splitted the country name/abbreviations from player's names.

## Data Processing:

- Processed the Span column which had year range of player's career span and converted that column to two new columns for Player's career Start Year and Final Year.
- Dropped the Span column cuz we no longer needed it.
- Separated the Player's names from Country names/abbreviations in the Player column and stored countries into a new column.
- Removed additional circle around the countries names.
- Calculated each player's career length by the diff of start year & end year, stored the resultant values into a new column called Career_Length of a Player.

- *Calculations on the dataframe after making new columns with the existing data:*
    - Average career length of players.
    - Average batting strike rate for players who played more than 10 years.
    - Players who played before year 2000, and players who played after 2000.
    - Players with the highest score group by country in test innings.
    - Top 10 players with the highest score in an innings in tests.
    - Top 10 players with the highest strike rate in an innings in tests.
    - Top 10 players with the batting average rate in an innings in tests.







 

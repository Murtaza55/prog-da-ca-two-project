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

- Starting to Work on cleaning the Cricket Data.
 

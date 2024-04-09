import requests
from bs4 import BeautifulSoup

# Cricket Test Matches Records
url = "https://www.espncricinfo.com/records/highest-career-batting-average-282910"

response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.content, "html.parser")

    table = soup.find("table", class_="ds-table")

    if table:
        print("Table found!")
        
    else:
        print("Table not found!")

    data = []
        
    # Finding the header rows to extract column names
    header_rows = table.find("thead").find_all("tr")

    column_names = []   
    for row in header_rows:
        divs = row.find_all("div")
        for div in divs:
            spans = div.find_all("span")
            for span in spans:
                column_names.append(span.text.strip())

    # Finding all the rows in the table body
    rows = table.find("tbody").find_all("tr")

    for row in rows:
        row_data = [td.text.strip() for td in row.find_all("td")]

        # Creating a dictionary mapping column names to row values
        row_dict = dict(zip(column_names, row_data))

        # Appending the data to the list
        data.append(row_dict)

import requests
from bs4 import BeautifulSoup

# Cricket Test Matches Records
url = "https://www.espncricinfo.com/records/highest-career-batting-average-282910"

# Send a GET request to the URL
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.content, "html.parser")

    table = soup.find("table", class_="ds-table")

    if table:
        print("Table found!")
    else:
        print("Table not found!")

# print(response)
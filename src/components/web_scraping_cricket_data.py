import requests
from bs4 import BeautifulSoup

url = "https://www.espncricinfo.com/records/highest-career-batting-average-282910"

# Send a GET request to the URL
response = requests.get(url)

print(response)
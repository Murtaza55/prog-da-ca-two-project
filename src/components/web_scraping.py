import requests
from bs4 import BeautifulSoup

# Dublin bus data
url = "https://gtfs.pro/en/ireland/transport-for-ireland/google-transit-combined/routes?type=Bus"

response = requests.get(url)

print(response)
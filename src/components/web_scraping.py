import requests
from bs4 import BeautifulSoup

routes_without_duplicates = ['1', '11', '116', '118', '120', '122', '123', '13', '130', '14', '140', '142', '145', '15', '150', '151', '155', '15A', '15B', '15D', '16', '16D', '26', '27', '27A', '27B', '27X', '32X', '33', '33D', '33E', '33X', '37', '38', '38A', '38B', '38D', '39', '39A', '39X', '4', '40', '40B', '40D', '40E', '41', '41B', '41C', '41D', '41X', '42', '42D', '43', '44', '44B', '46A', '46E', '47', '49', '51D', '52', '53', '54A', '56A', '6', '60', '61', '65', '65B', '68', '68A', '69', '69X', '7', '70', '70D', '77A', '77X', '7A', '7B', '7D', '83', '83A', '84', '84A', '84X', '9', 'C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'G1', 'G2', 'H1', 'H2', 'H3', 'L53', 'L54', 'L58', 'L59', 'N4', 'P29', 'X25', 'X26', 'X27', 'X28', 'X30', 'X31', 'X32']

routes = routes_without_duplicates

# Dublin bus data
url = "https://gtfs.pro/en/ireland/transport-for-ireland/google-transit-combined/routes?type=Bus"

def extract_bus_routes_links(url):
    try:

        response = requests.get(url)

        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')

            links = soup.find_all('a', class_='row-details-block')

            routes_links=[]
            for link in links:
                href = link.get('href')
                routes_links.append('https://gtfs.pro/'+href)
            return routes_links

    except requests.exceptions.RequestException as e:
      print("Failed to retrieve data from the URL:", e)
      return None
    
def extract_bus_stops(url):
    try:
        response = requests.get(url)

        response.raise_for_status()

        # Parse the HTML content
        soup = BeautifulSoup(response.text, 'html.parser')

        stop_elements = soup.find_all('th', class_='stop-name')

        stop_title = soup.find_all('h1', class_='title-page no-ellipsis')


        bus_stops = [stop.text.strip() for stop in stop_elements]

        return bus_stops
    except requests.exceptions.RequestException as e:
        print("Failed to retrieve data from the URL:", e)
        return None

def extract_route_title(url):
    try:
        response = requests.get(url)

        response.raise_for_status()

        soup = BeautifulSoup(response.text, 'html.parser')

        title_element = soup.find('h1', class_='title-page')

        route_title = title_element.text.strip() if title_element else None

        return route_title
    except requests.exceptions.RequestException as e:
        print("Failed to retrieve data from the URL:", e)
        return None
    
URL = "https://gtfs.pro/en/ireland/transport-for-ireland/google-transit-combined/routes?type=Bus"
bus_routes_links_array = extract_bus_routes_links(URL)

buss_stops_arr=[]
for link in bus_routes_links_array:
  bus_stops = extract_bus_stops(link)

import csv

# Read the data from the CSV file
with open('unique_bus_stops.csv', 'r') as file:
    reader = csv.reader(file)
    bus_stops = list(reader)

# Modify the bus stop names
modified_bus_stops = []
for bus_stop in bus_stops:
    modified_bus_stop = '-'.join(bus_stop).replace(' ', '-')
    modified_bus_stops.append(modified_bus_stop)

array = modified_bus_stops
links_array = []
url_template = "https://gtfs.pro/en/ireland/transport-for-ireland/google-transit-combined/stops?page={}"


with open('links.txt', 'w') as f:
    for page_num in range(1, 15):
        url = url_template.format(page_num)
        response = requests.get(url)

        if response.status_code == 200:
            html_content = response.text
            soup = BeautifulSoup(html_content, "html.parser")

            links = soup.find_all("a")

            printed_links = set()

            for link in links:
                href = link.get("href")
                if href:
                    if any(name in href for name in array):
                        if href not in printed_links:
                            full_href = "https://gtfs.pro/" + href
                            f.write(full_href + '\n')
                            printed_links.add(href)
                            links_array.append(full_href)
        else:
            print("Failed to fetch the HTML content for page", page_num, ". Status code:", response.status_code)

print("Links stored in array:", links_array)

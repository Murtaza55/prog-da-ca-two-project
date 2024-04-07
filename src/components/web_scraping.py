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
    
URL = "https://gtfs.pro/en/ireland/transport-for-ireland/google-transit-combined/routes?type=Bus"
bus_routes_links_array = extract_bus_routes_links(URL)

print('==========================Testing Routes=============================')
print('\n')
print('\n')
print('\n')
print('\n')
print('\n')
print('\n')

print(bus_routes_links_array)
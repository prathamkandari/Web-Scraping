import requests
from bs4 import BeautifulSoup
import json

url = 'https://www.ucobank.com/English/locator.aspx'

# Set a custom user agent (optional, if needed)
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36'
}

# Send an HTTP GET request to the URL
response = requests.get(url, headers=headers)

list = []

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content with Beautiful Soup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Output the HTML content (you can save it to a file or process it further)
    # print(soup.prettify())

    print("Below are list of services that ucobank provides to its customers: ")

    for link in soup.find_all('div',class_='megaMenu-single'):
        for link2 in link.find_all('h5'):
                list.append(link2.get_text())
        # list2.append(link.get('href'))

    for i in set(list):
        print(i)


else:
    print(f"Failed to fetch the page. Status code: {response.status_code}")

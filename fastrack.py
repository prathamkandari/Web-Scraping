import requests
from bs4 import BeautifulSoup
import json

url = 'https://www.fastrack.in/store-locator/find'

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

    script_tag = soup.find('script', type='application/ld+json')
    # print(script_tag)

    # Extract the JSON data from the <script> tag
    json_data = json.loads(script_tag.contents[0])

    # # Access the "sameAs" key in the JSON data to get the list of URLs
    social_media_urls = json_data.get('sameAs', [])
    
    # # Output the URLs   
    for url in social_media_urls:
        print(url)

else:
    print(f"Failed to fetch the page. Status code: {response.status_code}")

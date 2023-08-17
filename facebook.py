import requests
from bs4 import BeautifulSoup
import json

# URL of the page containing the script tag with JSON data
url = "https://www.facebook.com/uttarakhandpolice/"

# Send an HTTP GET request to the URL
response = requests.get(url)
html_content = response.content

# Parse the HTML content using Beautiful Soup
soup = BeautifulSoup(html_content, 'html.parser')

# Find the script tag containing the JSON data
script_tag = soup.find('script', attrs={"type": "application/json", "data-sigil": "context-hp-frontend"})

# Extract the content of the script tag
script_content = script_tag.string

# Clean the script content to extract the JSON data
json_start = script_content.index("{")
json_end = script_content.rindex("}") + 1
json_data = script_content[json_start:json_end]

# Parse the JSON data
data = json.loads(json_data)

# Print the data to understand its structure
print(data)

# Extract the followers count (update the keys according to the actual structure)
followers_count = parsed_data.get("user", {}).get("profile_social_context", {}).get("content", [])[0].get("text", {}).get("text", "").split()[0]
followers_count = int(followers_count.replace(",", ""))
print(f"Followers count: {followers_count}")


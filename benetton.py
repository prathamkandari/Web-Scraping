import requests
from bs4 import BeautifulSoup
import csv
import pandas as pd

url = "https://in.benetton.com/store-locator"
response = requests.get(url)

list1 = []
list2 = []
list3 = []

soup = BeautifulSoup(response.content, 'html.parser')

li_elements = soup.find_all('li', class_='text-list')
for li in li_elements:
    # Find all the anchor (a) elements within the li and get the href, text, and data-currency
    anchor = li.find('a')
    if anchor:
        href1 = anchor.get('href')
        href2 = anchor.get_text(strip=True)  # Use get_text() without 'href'
        href3 = anchor.get('data-currency')
        list1.append(href1)
        list2.append(href2)
        list3.append(href3)

# Prepare the data as a list of lists, where each inner list contains one row's data
data = list(zip(list1, list2, list3))

fields = ['Links', 'Locations', 'Currency']
with open('Benetton.csv', 'w+', newline='', encoding='utf-8') as f:  # Specify utf-8 encoding
    csv_writer = csv.writer(f)
    csv_writer.writerow(fields)

    # Write the list of lists to the CSV file
    csv_writer.writerows(data)

# Optionally, you can create a DataFrame and save it to CSV
df = pd.DataFrame(data, columns=fields)
df.to_csv('Benetton.csv', index=False, encoding='utf-8')  # Specify utf-8 encoding

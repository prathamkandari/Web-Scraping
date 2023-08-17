import requests
from bs4 import BeautifulSoup
import csv
import pandas as pd

url = "https://www.kia.com/in/buy/find-a-dealer.html"
response = requests.get(url)

list1 = []
list2 = []

soup = BeautifulSoup(response.content, 'html.parser')

ul_elements = soup.find_all('ul', class_='social-list')
for ul in ul_elements:
    li_elements = ul.find_all('li')
    for li in li_elements:
        anchor = li.find('a')
        if anchor:
            href = anchor.get('href')
            list1.append(href)

            anchor2 = anchor.find('span')
            if anchor2:
                href2 = anchor2.get_text()
                list2.append(href2)
            else:
                list2.append('')  # If no social media handle found, add an empty string

# Prepare a list of lists, each containing one link and its corresponding social media handle
data = list(zip(list1, list2))

fields = ['Links', 'Social Media Handles']
with open('kia.csv', 'w+', newline='') as f:
    csv_writer = csv.writer(f)
    csv_writer.writerow(fields)

    # Write the list of lists to the CSV file
    csv_writer.writerows(data)

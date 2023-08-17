import requests
from bs4 import BeautifulSoup
import csv
import pandas as pd

url = "https://www.libertyshoes.com/store-locator/"
response = requests.get(url)

list1 = []
list2 = []

soup = BeautifulSoup(response.content, 'html.parser')

# Find all the ul elements
ul_elements = soup.find_all('ul')

for ul in ul_elements:
    # Find all the li elements within the ul
    li_elements = ul.find_all('li')
    for li in li_elements:
        # Find all the anchor (a) elements within the li and get the href
        anchor = li.find('a')
        if anchor:
            href = anchor.get('href')
            href2 = anchor.get_text('href')
            list1.append(href)
            list2.append(href2)

# for i in set(list1):
#     print(i)

# for i in set(list2):
#     print(i)

fields= ['Contents']
with open('Liberty.csv', 'w+') as f:
    csv_writer = csv.writer(f)
    csv_writer.writerow(fields)
    csv_writer.writerow(list1)

df = pd.DataFrame(list1, columns=['Links'])
df2 =pd.DataFrame(list2, columns=['Description'])
merged_df = pd.concat([df, df2], axis=1)
merged_df.to_csv('Liberty.csv', index=False)
import requests
from bs4 import BeautifulSoup
import csv
import pandas as pd

url = "https://www.upesmtc.com/Team.html"
response = requests.get(url)

r = requests.get(url)
htmlContent = r.content

list1=[]
list2=[]

soup = BeautifulSoup(htmlContent, 'html.parser')

for i in soup.find_all('a',target="_blank"):
    list1.append(i.get_text())

for position in soup.find_all('div',class_='details'):
        for pos in position.find_all('p'):
            list2.append(pos.get_text())

fields= ['TEAM MEMBERS']
with open('CSV File2.csv', 'w+') as f:
    csv_writer = csv.writer(f)
    csv_writer.writerow(fields)
    csv_writer.writerow(list1)

df = pd.DataFrame(list1, columns=['Team Members Name'])
df2 =pd.DataFrame(list2, columns=['Team Members Position'])
merged_df = pd.concat([df, df2], axis=1)
merged_df.to_csv('CSV File2.csv', index=False)
# df2.to_csv('CSV File2.csv')
# df.to_csv('CSV File2.csv')
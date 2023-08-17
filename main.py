import requests
from bs4 import BeautifulSoup
url = "https://www.instagram.com/uttarakhandpolice/"

# For getting the HTMl
r = requests.get(url)
htmlContent = r.content
# print(htmlContent)
# HTML parser
soup = BeautifulSoup(htmlContent, 'html.parser')
# print(soup.prettify)

# title=soup.title
# print(title)

list = []
list2 = []
list3 = []
list4 = []
# Printing the first para of the upes csa

# print(soup.find_all("meta", class_="content"))
meta_description = soup.find('meta', attrs={'name': 'description'})

# Extract the content attribute from the <meta> tag
description_content = meta_description['content']

# Print the extracted description content
list = description_content
list2 = list.split(',')[0]
list3 = list.split(',')[1]
list4 = list[30:41]
print(list2)
print(list3) 
print(list4) 


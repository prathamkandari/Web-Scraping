import requests
from bs4 import BeautifulSoup
url = "https://upescsa.in/"
response = requests.get(url)

r = requests.get(url)
htmlContent = r.content
# print(htmlContent)

if response.status_code == 200:
    soup = BeautifulSoup(htmlContent, 'html.parser')
# print(soup.prettify)

    title=soup.title
# print(title)

    list2 = []

    for link in soup.find_all('div',class_='social'):
        for link2 in link.find_all('a'):
            for link3 in link2:
                list2.append(link2.get('href'))
        # list2.append(link.get('href'))

    for i in set(list2):
        print(i)

else:
    print("Failed to retrieve the webpage.")

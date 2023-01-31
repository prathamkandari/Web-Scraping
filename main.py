import requests
from bs4 import BeautifulSoup
url = "https://www.upescsa.in/"

# For getting the HTMl
r = requests.get(url)
htmlContent = r.content
print(htmlContent)
# HTML parser
# soup = BeautifulSoup(htmlContent, 'html.parser')
# print(soup.prettify)

# title=soup.title
# print(title)


# Printing the first para of the upes csa

# print(soup.find_all("p", class_="content"))
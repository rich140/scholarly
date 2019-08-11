import requests
import urllib.request
import time
from bs4 import BeautifulSoup


url = "https://www.nature.com/search?order=date_desc&article_type=research%2Creviews%2Cprotocols&subject=biological-sciences"
response = requests.get(url)
# print(response)


soup = BeautifulSoup(response.text, "html.parser")

a_tags = soup.findAll('a')
# print(type(soup))

# for link in soup.find_all('a'):
#     print(link.get('href'))


def removeNoText(lst):
    arr = []
    for i in range(0, len(lst)):
        if (lst[i].getText() != ""):
            arr.append(lst[i])
    return arr


textOnly = removeNoText(a_tags)

for i in range(0, len(textOnly)):
    if (len(textOnly[i].getText()) > 85):
        print(textOnly[i].getText())
        print(textOnly[i].get('a'))
        print("-----------------------------------------------------------")


# <a data-track = "click" data-track-action = "search result" data-track-label = "rank 0"
# href = "/articles/s41598-019-48098-0" itemprop = "url" >
#                 Manipulating the visibility of barriers to improve spatial
#                 navigation efficiency and cognitive mapping
#             </a>

import requests
import urllib.request
import time
from bs4 import BeautifulSoup


nature_urls = ["https://www.nature.com/search?order=date_desc&article_type=research%2Creviews%2Cprotocols&subject=biological-sciences",
               "https://www.nature.com/search?order=date_desc&article_type=research%2Creviews%2Cprotocols&subject=scientific-community-and-society",
               "https://www.nature.com/search?order=date_desc&article_type=research%2Creviews%2Cprotocols&subject=earth-and-environmental-sciences",
               "https://www.nature.com/search?order=date_desc&article_type=research%2Creviews%2Cprotocols&subject=health-sciences",
               "https://www.nature.com/search?order=date_desc&article_type=research%2Creviews%2Cprotocols&subject=physical-sciences"]


def removeNoText(lst):
    arr = []
    for i in range(0, len(lst)):
        if (lst[i].getText() != ""):
            arr.append(lst[i])
    return arr


def filter(soup):
    a_tags = soup.findAll('a')
    all_articles = removeNoText(a_tags)
    titles, links = [], []
    for article in all_articles:
        if (len(article.getText()) > 85 and article.getText().startswith("Rights") == False):
            titles.append(article.getText().strip())
            if (("nature.com" in article['href']) == False):
                links.append("http://www.nature.com" + article['href'])
            else:
                links.append(article['href'])
    return titles, links


for url in nature_urls:
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    titles, links = filter(soup)
    # TO PRINT:
#     for title in titles:
#         print(title)
#     for link in links:
#         print(links)

import requests
import urllib.request
import time
from bs4 import BeautifulSoup
from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

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
    result = {}
    for article in all_articles:
        if (len(article.getText()) > 85 and article.getText().startswith("Rights") == False):
            if (("nature.com" in article['href']) == False):
                result[article.getText().strip()] = "http://www.nature.com" + \
                    article['href']
            else:
                result[article.getText().strip()] = article['href']
    return result


def extract():
    result = []
    for url in nature_urls:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        result.append(filter(soup))
    return result

# TO PRINT:
# for key, val in result.items():
#     print(key, "=>", val)


@app.route("/")
def info():
    return render_template('index.html', author="Me", data=extract())


if __name__ == '__main__':
    app.run()

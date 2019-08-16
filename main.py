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


nejm_urls = ["https://www.nejm.org/medical-articles/original-article#qs=%3Farticletype%3Doriginal-article%26requestType%3Dajax%26%26topic%3D2%26viewClass%3D%26searchType%3Dcme%26manualFilterParam%3DsearchType_delimiter_searchType_delimiter_topic_delimiter_topic_delimiter_topic_delimiter_contentAge_delimiter_contentAge_delimiter_topic_firstDelimiter"]


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


response = requests.get(nejm_urls[0])
soup = BeautifulSoup(response.text, "html.parser")
strong_tags = soup.findAll('strong')
print(len(strong_tags))
# print(soup)
# for tag in strong_tags:
#     print(tag.getText())
#     print(len(tag.getText()))
#     print("------------------------------------------------------")


def filterNejm(soup):
    strong_tags = soup.findAll('strong')
    result = {}
    for i in range(30, len(strong_tags)):
        if(strong_tags[i].getText().startswith("\n") == False):
            result.append(strong_tags[i].getText())
    return result


def extractNejm():
    result = []
    for url in nejm_urls:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        result.append(filter(soup))
    return result


# print(filterNejm(soup))


# TO PRINT:
# for key, val in result.items():
#     print(key, "=>", val)


# @app.route('/')
# def info():
#     return render_template('index.html', author="Me", data=extract())


# if __name__ == '__main__':
#     app.run()

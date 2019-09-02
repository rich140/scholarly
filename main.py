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

ncom_urls = ["https://www.nature.com/subjects/biological-sciences/ncomms"]

plos_urls = [
    "https://journals.plos.org/plosone/browse/medicine_and_health_sciences"]

scireports_urls = ["https://www.nature.com/subjects/biological-sciences/srep"]

sciadv_urls = ["https://advances.sciencemag.org"]


def removeNoText(lst):
    arr = []
    for i in range(0, len(lst)):
        if (lst[i].getText() != ""):
            arr.append(lst[i])
    return arr


def filter_nature(soup):
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


def extract_nature():
    result = []
    for url in nature_urls:
        # response = requests.get(url)
        # soup = BeautifulSoup(response.text, "html.parser")
        # result.append(filter_nature(soup))
        dict = {}
        result.append(dict)
    return result


# response = requests.get(nejm_urls[0])
# soup = BeautifulSoup(response.text, "html.parser")
# a_tags = soup.findAll('a')
# print(len(a_tags))
# for tag in a_tags:
#     if (tag.find('strong')):
#         strong_tags =
#         print(tag.getText())
#         print(len(tag.getText()))
#         print("------------------------------------------------------")


def filter_nejm(soup):
    strong_tags = soup.findAll('strong')
    result = {}
    for i in range(30, len(strong_tags)):
        if(strong_tags[i].getText().startswith("\n") == False):
            result[strong_tags[i].getText()] = "http://www.nejm.org" + \
                strong_tags[i].parent.parent['href'].rstrip(',')
    return result


def extract_nejm():
    result = []
    for url in nejm_urls:
        # response = requests.get(url)
        # soup = BeautifulSoup(response.text, "html.parser")
        # result.append(filter_nejm(soup))
        dict = {}
        result.append(dict)
    return result


def filter_ncom(soup):
    a_tags = soup.findAll('a')
    result = {}
    for tag in a_tags:
        if(len(tag.getText().strip()) > 85):
            result[tag.getText().strip()] = "http://www.nature.com" + \
                tag['href']
    return result


def extract_ncom():
    result = []
    for url in ncom_urls:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        result.append(filter_ncom(soup))
    return result


def filter_plos(soup):
    a_tags = soup.findAll('a')
    result = {}
    for tag in a_tags:
        if (len(tag.getText().strip()) > 85 and (tag.getText().strip().startswith('Retraction') == False)):
            result[tag.getText().strip()] = "https://journals.plos.org" + \
                tag['href']
    return result


def extract_plos():
    result = []
    for url in plos_urls:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        result.append(filter_plos(soup))
    return result


def filter_scireports(soup):
    a_tags = soup.findAll('a')
    result = {}
    for tag in a_tags:
        if(len(tag.getText().strip()) > 85):
            result[tag.getText().strip()] = "http://www.nature.com" + \
                tag['href']
    return result


def extract_scireports():
    result = []
    for url in scireports_urls:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        result.append(filter_scireports(soup))
    return result


def filter_sciadv(soup):
    a_tags = soup.findAll('a')
    result = {}
    for tag in a_tags:
        if(len(tag.getText().strip()) > 60):
            result[tag.getText().strip()] = "https://advances.sciencemag.org" + \
                tag['href']
    return result


def extract_sciadv():
    result = []
    for url in sciadv_urls:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        result.append(filter_sciadv(soup))
    return result


# for thing in extract_ncom():
#     print(thing)


# TO PRINT:
# for key, val in result.items():
#     print(key, "=>", val)


# RUN SERVER
@app.route('/')
def info():
    return render_template('index.html', author="Me", data=extract_nature(),
                           nejm=extract_nejm(), ncom=extract_ncom(), plos=extract_plos(),
                           scireports=extract_scireports(), sciadv=extract_sciadv())


if __name__ == '__main__':
    app.run()

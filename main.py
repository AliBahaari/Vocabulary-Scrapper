import requests as req
from bs4 import BeautifulSoup


def get_phrases(collection_url):

    data = req.get(collection_url)

    soup = BeautifulSoup(data.text, 'html.parser')

    words = []
    defintions = []

    for i in soup.find_all(class_="word"):
        words.append(i.text)

    for j in soup.find_all(class_="definition"):
        defintions.append(j.text)

    return list(zip(words, defintions))

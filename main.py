import requests as req
from bs4 import BeautifulSoup
from flask import Flask


app = Flask(__name__)


@app.route('/')
def get_home():
    return """
        Greetings!
        Just use /api/[COLLECTION_ID] endpoint to create an API for the collection you've specified from 'vocabulary.com'.
    """


@app.route('/api/<int:collection_id>')
def get_api(collection_id):

    request = req.get("https://www.vocabulary.com/lists/" + str(collection_id))

    if request.status_code == 200:

        soup = BeautifulSoup(request.text, 'html.parser')

        words = []
        defintions = []

        for i in soup.find_all(class_="word"):
            words.append(i.text)

        for j in soup.find_all(class_="definition"):
            defintions.append(j.text)

        obj = {}

        for k, l in zip(words, defintions):
            obj[k] = l

        return obj

    else:
        return "Collection ID isn't valid"

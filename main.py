#Flask
from flask import Flask
from flask.app import Flask as FlaskApp

#other
import requests
from requests.models import Response


app: FlaskApp = Flask(__name__)
cards: list[dict] = []

@app.route("/")
def main_page() -> str:
    return cards


if __name__ == '__main__':
    URL: str = (
        'https://api.hearthstonejson.com/'
        'v1/121569/ruRU/cards.collectible.json'
    )
    response: Response =\
        requests.get(URL)
    data: list[dict] = response.json()
    for card in data:
        cards.append(card)

    app.run(
        port=8080,
        debug=True
    )


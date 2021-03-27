from flask import Flask, render_template
from src import spotify_api
import json


app = Flask(__name__)


def start():
    app.run(host="0.0.0.0")


@app.route('/')
def home():
    return render_template('home.html')

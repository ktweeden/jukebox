from flask import Flask, render_template, redirect, request
from flask_cors import CORS
from .api import spotify_api


app = Flask(__name__)
CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


def start():
    app.run(host="0.0.0.0")


@app.route('/', methods=['GET'])
def home():
    return render_template('home.html')


@app.route('/authenticate', methods=['GET'])
def authenticate():
    api = spotify_api.SpotifyApi()
    auth_url = api.authorization_url()
    print(auth_url)
    return redirect(auth_url)


@app.route('/spotify', methods=['GET'])
def spotify():
    api = spotify_api.SpotifyApi()
    code = request.args.get('code')
    print("code: " + code)
    api.get_access_token(code)
    return redirect('/')

import requests
import json
import os

SPOTIFY_API_ID = os.getenv("SPOTIFY_API_ID")
SPOTIFY_API_KEY = os.getenv("SPOTIFY_API_KEY")


class SpotifyApi:
    def __init__(self):
        self.base_url = "https://api.spotify.com"

    def get_artist_details(self, artist_id):
        url = self.base_url+"/v1/artists/"+artist_id
        headers = {"Authorization": "Bearer " + str(SPOTIFY_API_KEY)}
        print url
        response = requests.get(url, headers=headers)
        print response.text

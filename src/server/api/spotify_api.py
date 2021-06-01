import requests
import os
import base64


class SpotifyApi:
    def __init__(self):
        self.base_auth_url = "https://accounts.spotify.com"
        self.spotify_api_id = os.environ.get("SPOTIFY_API_ID")
        self.spotify_api_key = os.environ.get("SPOTIFY_API_KEY")
        self.auth_redirect_uri = os.environ.get("AUTH_REDIRECT_URI")

    def authorization_url(self):
        return self.base_auth_url+"/authorize?client_id="+self.spotify_api_id+"&response_type=code&redirect_uri="+self.auth_redirect_uri+"&scope=user-read-private streaming user-library-read playlist-read-private user-read-currently-playing"

    def get_access_token(self, code):
        auth_string = bytes('{}:{}'.format(
            self.spotify_api_id, self.spotify_api_key), 'utf-8')
        encoded_auth_string = base64.b64encode(
            auth_string).decode()
        data = {
            "code": code,
            "redirect_uri": self.auth_redirect_uri,
            "grant_type": "authorization_code"
        }
        headers = {
            "Authorization": "Basic " + encoded_auth_string
        }

        response = requests.post(
            "https://accounts.spotify.com/api/token", data=data, headers=headers)

        response_data = response.json()
        print(response_data)
        access_token = response_data['access_token']
        # TODO: Where to store access token, what to do with refresh token?
        # TOOD: Handle error response (response_data['error'])

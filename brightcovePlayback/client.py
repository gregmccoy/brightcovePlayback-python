import requests
import json
from brightcovePlayback.video import Video
from brightcovePlayback.playlist import Playlist

class PlaybackClient(object):

    def __init__(self, token, account_id):

        self.token = token
        self.account_id = account_id
        self.headers = { "BCOV-Policy": self.token }
        self.video = Video(self)
        self.playlist = Playlist(self)
        self.contenttype = "application/x-www-form-urlencoded"


    def call_api(self, endpoint, method, data=None, files=None):
        if method == "POST":
            response = requests.post(endpoint, headers=self.headers, data=data, files=files)
        elif method == "PUT":
            response = requests.put(endpoint, headers=self.headers, data=data, files=files)
        elif method == "GET":
            response = requests.get(endpoint, headers=self.headers, data=data)
        elif method == "DELETE":
            response = requests.delete(endpoint, headers=self.headers, data=data)
        else:
            raise Exception("Method not supported")

        if response.status_code != 200 and response.status_code != 201:
            raise requests.ConnectionError("Expected status code 200, but got {}".format(response.status_code))
        return_data = ""
        return response.json()

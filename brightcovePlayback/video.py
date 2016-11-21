class Video(object):

    def __init__(self, client):
        self.client = client


    def get(self, id=""):
        return self.client.call_api("https://edge.api.brightcove.com/playback/v1/accounts/" + self.client.account_id + "/videos/" + id, "GET")


    def search(self, search):
        return self.client.call_api("https://edge.api.brightcove.com/playback/v1/accounts/" + self.client.account_id + "/videos/?q=" + search, "GET")


    def sources(self, id):
        return self.client.call_api("https://edge.api.brightcove.com/playback/v1/accounts/" + self.client.account_id + "/videos/" + id + "/sources/", "GET")


    def playlists(self, id):
        return self.client.call_api("https://edge.api.brightcove.com/playback/v1/accounts/" + self.client.account_id + "/videos/" + id + "/references/", "GET")

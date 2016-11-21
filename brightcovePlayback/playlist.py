class Playlist(object):

    def __init__(self, client):
        self.client = client


    def get(self, id=""):
        if id != "":
            id = id + "/"
        return self.client.call_api("https://edge.api.brightcove.com/playback/v1/accounts/" + self.client.account_id + "/playlists/" + id, "GET")


    def search(self, search):
        return self.client.call_api("https://edge.api.brightcove.com/playback/v1/accounts/" + self.client.account_id + "/playlists/?q=" + search, "GET")

    def videos(self, id):
        playlist = self.client.call_api("https://edge.api.brightcove.com/playback/v1/accounts/" + self.client.account_id + "/playlists/" + id, "GET")
        video_list = { "videos": [], "image": [] }
        for video in playlist["video_ids"]:
            response = self.client.call_api("https://edge.api.brightcove.com/playback/v1/accounts/" + self.client.account_id + "/videos/" + str(video), "GET")
            video_list["videos"].append(response)
            video_list["image"].append(response["images"]["poster"]["sources"][0]["src"])
        return video_list


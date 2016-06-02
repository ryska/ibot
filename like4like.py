import json
import urllib2
from bottle import request


class Like4Like:

    def __init__(self, media_count):
        self.media_count = media_count
        self.api_media_likes = "https://api.instagram.com/v1/media/%s/likes?access_token=%s"
        self.api_recent_media = "https://api.instagram.com/v1/users/self/media/recent/?access_token=%s"
        self.access_token = request.session['access_token']

    def fill_media_list(self, jsonik, media_list):
        for i in jsonik["data"]:
            media_list.append(i["id"])
        return media_list

    def get_media_id_list(self):
        url = self.api_recent_media % self.access_token
        response = urllib2.urlopen(url).read()
        json_response = json.loads(response)
        media = []
        media = self.fill_media_list(json_response, media)
        if self.media_count > 20:
            for i in range(self.how_many()):
                self.api_recent_media_tmp = json_response["pagination"]["next_url"]
                response = urllib2.urlopen(self.api_recent_media_tmp).read()
                json_response = json.loads(response)
                media = self.fill_media_list(json_response, media)
        return media

    def how_many(self):
        tmp = self.media_count - 20
        how_many = tmp / 20
        if (tmp % 20) > 0:
            how_many = how_many + 1
            return how_many
        else
            return how_many

    def get_list_of_users_who_liked_media(self, media):
        users_lists = []
        for i in range(media.__len__()):
            url = self.api_media_likes % (media[i], access_token)
            response = urllib2.urlopen(url).read()
            json_response = json.loads(response)
            if json_response["data"]:
                for i in json_response["data"]:
                    if i["id"] not in users_lists:
                        users_lists.append(i["id"])
        return users_lists
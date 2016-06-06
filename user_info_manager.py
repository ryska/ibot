from instagram import client
from config import CONFIG
from bottle import request
import requests
import json

class UserInfo:
    '''
    This class try to take some user info (following, followers, etc.)
    '''
    user_agent = ("Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 "
                  "(KHTML, like Gecko) Chrome/48.0.2564.103 Safari/537.36")

    url_list = {
                "ink361":
                     {
                      "main": "http://ink361.com/",
                      "user": "http://ink361.com/app/users/%s",
                      "search_name": "https://data.ink361.com/v1/users/search?q=%s",
                      "search_id": "https://data.ink361.com/v1/users/ig-%s",
                      "followers": "https://data.ink361.com/v1/users/ig-%s/followed-by",
                      "following": "https://data.ink361.com/v1/users/ig-%s/follows",
                      "stat": "http://ink361.com/app/users/ig-%s/%s/stats"
                     }
               }

    def __init__(self, user_id, info_aggregator="ink361"):
        self.i_a = info_aggregator
        self.user_id = user_id
        self.hello()
        self.followed_by_count = 0
        self.followed_by = []

    def hello(self):
        self.s = requests.Session()
        self.s.headers.update({'User-Agent' : self.user_agent})
        main = self.s.get(self.url_list[self.i_a]["main"])
        if main.status_code == 200:
            return True
        return False

    def get_followed_by(self, limit=-1):
        self.followed_by = None
        self.followed_by = []
        if self.user_id:
            next_url = self.url_list[self.i_a]["followers"] % self.user_id
            while True:
                followed_by = self.s.get(next_url)
                r = json.loads(followed_by.text)
                for u in r["data"]:
                    if limit > 0 or limit < 0:
                        self.followed_by.append({
                            "username": u["username"],
                            # "profile_picture": u["profile_picture"],
                            "id": u["id"].split("-")[1],
                            # "full_name": u["full_name"]
                        })
                        limit -= 1
                    else:
                        return True
                if r["pagination"]["next_url"]:
                    # have more data
                    next_url = r["pagination"]["next_url"]
                else:
                    # end of data
                    return True
        return False

    def get_follows(self, limit=-1):
        self.follows = None
        self.follows = []
        if self.user_id:
            next_url = self.url_list[self.i_a]["following"] % self.user_id
            while True:
                follows = self.s.get(next_url)
                r = json.loads(follows.text)
                for u in r["data"]:
                    if limit > 0 or limit < 0:
                        self.follows.append({
                            "username": u["username"],
                            # "profile_picture": u["profile_picture"],
                            "id": u["id"].split("-")[1],
                            # "full_name": u["full_name"]
                        })
                        limit -= 1
                    else:
                        return True
                if r["pagination"]["next_url"]:
                    # have more data
                    next_url = r["pagination"]["next_url"]
                else:
                    # end of data
                    return True
        return False

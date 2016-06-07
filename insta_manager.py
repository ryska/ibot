from pic_manager import PicManager
import requests
import datetime
import logging
import json
import time


class InstaManager:

    url = 'https://www.instagram.com/'
    url_tag = 'https://www.instagram.com/explore/tags/'
    url_likes = 'https://www.instagram.com/web/likes/%s/like/'
    url_unlike = 'https://www.instagram.com/web/likes/%s/unlike/'
    url_comment = 'https://www.instagram.com/web/comments/%s/add/'
    url_follow = 'https://www.instagram.com/web/friendships/%s/follow/'
    url_unfollow = 'https://www.instagram.com/web/friendships/%s/unfollow/'
    url_login = 'https://www.instagram.com/accounts/login/ajax/'
    url_logout = 'https://www.instagram.com/accounts/logout/'

    user_agent = ("Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 "
                      "(KHTML, like Gecko) Chrome/48.0.2564.103 Safari/537.36")
    accept_language = 'pl;q=0.8,en-US;q=0.6,en;q=0.4'

    # Log setting.
    log_file_path = ''
    log_file = 0

    # Other.
    media_by_tag = 0
    login_status = False

    def __init__(self, login, password,
                 user_id,
                 tag_list,
                 log_mod = 0):

        # log_mod 0 to console, 1 to file
        self.log_mod = log_mod

        self.s = requests.Session()
        self.user_login = login.lower()
        self.user_password = password

        self.tag_list = tag_list
        self.user_id = user_id

        self.media_by_tag = []

        self.like_counter = 0
        self.unlike_counter = 0
        self.follow_counter = 0
        self.unfollow_counter = 0
        self.comments_counter = 0

        now_time = datetime.datetime.now()
        log_string = 'Starting at %s:' % \
                     (now_time.strftime("%d.%m.%Y %H:%M"))
        self.write_log(log_string)
        self.login()

        self.pic_manager = PicManager()

    def login(self):
            log_string = 'Try to login by %s...' % self.user_login
            self.write_log(log_string)
            self.s.cookies.update({'sessionid': '', 'mid': '', 'ig_pr': '1',
                                   'ig_vw': '1920', 'csrftoken': '',
                                   's_network': '', 'ds_user_id': ''})
            self.login_post = {'username': self.user_login,
                               'password': self.user_password}
            self.s.headers.update({'Accept-Encoding': 'gzip, deflate',
                                   'Accept-Language': self.accept_language,
                                   'Connection': 'keep-alive',
                                   'Content-Length': '0',
                                   'Host': 'www.instagram.com',
                                   'Origin': 'https://www.instagram.com',
                                   'Referer': 'https://www.instagram.com/',
                                   'User-Agent': self.user_agent,
                                   'X-Instagram-AJAX': '1',
                                   'X-Requested-With': 'XMLHttpRequest'})
            r = self.s.get(self.url)
            self.s.headers.update({'X-CSRFToken': r.cookies['csrftoken']})
            login = self.s.post(self.url_login, data=self.login_post,
                                allow_redirects=True)
            self.s.headers.update({'X-CSRFToken': login.cookies['csrftoken']})
            self.csrftoken = login.cookies['csrftoken']

            if login.status_code == 200:
                r = self.s.get('https://www.instagram.com/')
                finder = r.text.find(self.user_login)
                if finder != -1:
                    self.login_status = True
                    log_string = 'Look like login by %s succeedded!' % self.user_login
                    self.write_log(log_string)
                else:
                    self.login_status = False
                    self.write_log('Login error! Check your login data!')
            else:
                self.write_log('Login error! Connection error!')

    def logout(self):
        log_string = 'Logout: likes - %i, follow - %i, unfollow - %i, comments - %i.' % \
                     (self.like_counter, self.follow_counter,
                      self.unfollow_counter, self.comments_counter)
        self.write_log(log_string)

        try:
            logout_post = {'csrfmiddlewaretoken': self.csrftoken}
            logout = self.s.post(self.url_logout, data=logout_post)
            self.write_log("Logged out!")
            self.login_status = False
        except:
            self.write_log("Logout error!")

    # wyszukiwanie id mediow pasujacych do podanego taga
    def get_media_id_by_tag(self, tag):
        if self.login_status:
            log_string = "Get media id by tag: %s" % tag
            self.write_log(log_string)
            if self.login_status == 1:
                url_tag = '%s%s%s' % (self.url_tag, tag, '/')
                try:
                    r = self.s.get(url_tag)
                    text = r.text

                    finder_text_start = ('<script type="text/javascript">'
                                         'window._sharedData = ')
                    finder_text_start_len = len(finder_text_start) - 1
                    finder_text_end = ';</script>'

                    all_data_start = text.find(finder_text_start)
                    all_data_end = text.find(finder_text_end, all_data_start + 1)
                    json_str = text[(all_data_start + finder_text_start_len + 1) \
                        : all_data_end]
                    all_data = json.loads(json_str)

                    self.media_by_tag = list(all_data['entry_data']['TagPage'][0] \
                                                 ['tag']['media']['nodes'])

                    self.write_log("Found %d posts." % len(self.media_by_tag))
                except:
                    self.media_by_tag = []
                    self.write_log("Except while getting media by tag %s!" % tag)
            else:
                return 0

    def like(self, media_id):
        if self.login_status:
            url_likes = self.url_likes % media_id
            try:
                like = self.s.post(url_likes)
                self.like_counter += 1
                self.write_log("Liked media with id: %s" % media_id)
            except:
                self.write_log("Except while liking media with id: %s" % media_id)
                like = 0
            return like

    def unlike(self, media_id):
        if self.login_status:
            url_unlike = self.url_unlike % media_id
            try:
                unlike = self.s.post(url_unlike)
                self.unlike_counter += 1
                self.write_log("Unliked media with id: %s" % media_id)
            except:
                self.write_log("Except while unliking media with id: %s" % media_id)
                unlike = 0
            return unlike

    def follow(self, user_id):
        if self.login_status:
            url_follow = self.url_follow % user_id
            try:
                follow = self.s.post(url_follow)
                if follow.status_code == 200:
                    self.follow_counter += 1
                    log_string = "Followed user with id: %s." % user_id
                    self.write_log(log_string)
                return follow
            except:
                self.write_log("Except while following user with id: %s." % user_id)
        return False

    def unfollow(self, user_id):
        if self.login_status:
            url_unfollow = self.url_unfollow % user_id
            try:
                unfollow = self.s.post(url_unfollow)
                if unfollow.status_code == 200:
                    self.unfollow_counter += 1
                    log_string = "Unfollowed user with id: %s." % user_id
                    self.write_log(log_string)
                return unfollow
            except:
                self.write_log("Except while unfollowing user with id: %s." % user_id)
        return False

    def comment(self, media_id, comment_text):
        if self.login_status:
            comment_post = {'comment_text': comment_text}
            url_comment = self.url_comment % media_id
            try:
                comment = self.s.post(url_comment, data=comment_post)
                if comment.status_code == 200:
                    self.comments_counter += 1
                    log_string = 'Written: "%s" under post with id: %s.' % (comment_text, media_id)
                    self.write_log(log_string)
                return comment
            except:
                self.write_log("Except while commenting media with id %s!" % media_id)
        else:
            self.write_log("Login status error")
        return False

    def auto_mod(self):
        #ui_manager = UserInfo(self.user_id)

        self.write_log("Posting photo with tags from given category...")
        self.pic_manager.upload(self.tag_list)

        # szuka tylko po dwoch pierwszych tagach z tag_list. Do zmiany pozniej.
        for tag in self.tag_list[:2]:
            self.write_log("Searching media with tag %s" % tag)
            self.get_media_id_by_tag(tag)
            for media in self.media_by_tag:
                self.like(media['id'])
                self.follow(media['owner']['id'])

        self.write_log("Going to sleep for a minute...")
        time.sleep(60)

        # F4F - nie dziala w oddzielnym watku.
        """
        ui_manager.get_followed_by()

        if ui_manager.followed_by.__len__() > self.followed_by_count:
            self.write_log("I got new followers. Following back...")
            difference = ui_manager.followed_by.__len__() - self.followed_by_count
            while difference > 0:
                self.follow(ui_manager.followed_by[difference - 1]['id'])
                difference -= 1
        """

    def write_log(self, log_text):
        if self.log_mod == 0:
            try:
                print(log_text)
            except UnicodeEncodeError:
                print("Your text has unicode problem!")
        elif self.log_mod == 1:
        # Create log_file if not exist.
            if self.log_file == 0:
                self.log_file = 1
                now_time = datetime.datetime.now()
                self.log_full_path = '%s%s_%s.log' % (self.log_file_path,
                                                        self.user_login,
                                                        now_time.strftime("%d.%m.%Y_%H:%M"))
                formatter = logging.Formatter('%(asctime)s - %(name)s '
                                                      '- %(message)s')
                self.logger = logging.getLogger(self.user_login)
                self.hdrl = logging.FileHandler(self.log_full_path, mode='w')
                self.hdrl.setFormatter(formatter)
                self.logger.setLevel(level=logging.INFO)
                self.logger.addHandler(self.hdrl)
                # Log to log file.
                try:
                    self.logger.info(log_text)
                except UnicodeEncodeError:
                    print("Your text has unicode problem!")

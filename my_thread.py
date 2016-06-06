from insta_manager import InstaManager
import threading

class MyThread(object):
    def __init__(self, login, password, user_id, tag_list, log_mod):
        thread = threading.Thread(target=self.run, args=(login, password, user_id, tag_list, log_mod))
        thread.daemon = True
        thread.start()

    def run(self, login, password, user_id, tag_list, log_mod):
        bot = InstaManager(
            login,
            password,
            tag_list,
            log_mod)

        bot.user_id = user_id
        bot.auto_mod()
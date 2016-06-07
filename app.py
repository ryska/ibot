import bottle
import beaker.middleware
import os
from pic_manager import PicManager
from api_manager import ApiManager
from bottle import route, post, request, hook, template, static_file
from instagram import client, subscriptions
from config import CONFIG, unauthenticated_api
from my_thread import MyThread


bottle.debug(True)

session_opts = {
    'session.type': 'file',
    'session.data_dir': './session/',
    'session.auto': True,
}
app = beaker.middleware.SessionMiddleware(bottle.app(), session_opts)

pic_manager = PicManager()
api_manager = ApiManager()

@hook('before_request')
def setup_request():
    request.session = request.environ['beaker.session']

def process_tag_update(update):
    print(update)

@route('/static/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root='./static')


@route('/')
def home():
    try:
        url = unauthenticated_api.get_authorize_url(
            scope=["public_content", "comments", "likes", "follower_list", "basic", "relationships"])
        return template('index.tpl', url=url)
    except Exception as e:
        print(e)


@route('/upload')
def on_upload():
    tag_list = pic_manager.upload("buildings")
    return template('upload.tpl', tag_lists=tag_list)

@route('/oauth_callback')
def on_callback():
    code = request.GET.get("code")
    if not code:
        return 'Missing code'
    try:
        access_token, user_info = unauthenticated_api.exchange_code_for_access_token(code)
        if not access_token:
            return 'Could not get access token'
        request.session['access_token'] = access_token
        api_manager.start()
    except Exception as e:
        print(e)
    return template('menu')

@route('/tag_search')
def on_tag_search():
    tag_list = pic_manager.get_tags('Urban', 10)
    user_id = api_manager.get_user_id()
    thread = MyThread("urbanshot__", "kluza1", user_id, tag_list, 0)

    # zakomentowane bo nie ma instancji bota.

    # ui_manager = UserInfo(get_user_id())
    # ui_manager.followed_by_count = int(get_followed_by_count())
    #
    # time.sleep(30)
    #
    # followed_by_count = int(get_followed_by_count())
    # print 'Followed by before: %d' % ui_manager.followed_by_count
    # print 'Followed by after: %d' % followed_by_count
    #
    # if followed_by_count > ui_manager.followed_by_count:
    #     difference = followed_by_count - ui_manager.followed_by_count
    #     ui_manager.get_followed_by()
    #     while difference > 0:
    #         bot.follow(ui_manager.followed_by[difference - 1]['id'])
    #         bot.unfollow(ui_manager.followed_by[difference - 1]['id'])
    #         difference -= 1
    #
    # return template('data',
    #             posts=api_manager.get_media_count(),
    #             following=api_manager.get_follows_count(),
    #             followed=api_manager.get_followed_by_count()
    #                 )

@route('/realtime_callback')
@post('/realtime_callback')
def on_realtime_callback():
    reactor = subscriptions.SubscriptionsReactor()
    reactor.register_callback(subscriptions.SubscriptionType.TAG, process_tag_update)

    mode = request.GET.get("hub.mode")
    challenge = request.GET.get("hub.challenge")
    verify_token = request.GET.get("hub.verify_token")
    if challenge:
        return challenge
    else:
        x_hub_signature = request.header.get('X-Hub-Signature')
        raw_response = request.body.read()
        try:
            reactor.process(CONFIG['client_secret'], raw_response, x_hub_signature)
        except subscriptions.SubscriptionVerifyError:
            print("Signature mismatch")


port = int(os.environ.get('PORT', 5000))

bottle.run(app=app, host='localhost', port=port, reloader=True)

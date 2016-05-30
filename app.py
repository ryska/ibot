import bottle
import beaker.middleware
from pic_manager import upload
from insta_manager import get_followed_by_count, get_follows_count, InstaManager
from user_info_manager import UserInfo
from bottle import route, post, request, hook, template, static_file
from instagram import client, subscriptions
from config import CONFIG, unauthenticated_api
import time


bottle.debug(True)

session_opts = {
    'session.type': 'file',
    'session.data_dir': './session/',
    'session.auto': True,
}

app = beaker.middleware.SessionMiddleware(bottle.app(), session_opts)



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
        url = unauthenticated_api.get_authorize_url(scope=["public_content","comments","likes","follower_list","basic","relationships"])
        return template('index', url=url)
    except Exception as e:
        print(e)


@route('/upload')
def on_upload():
    tag_list = upload("buildings")
    return template('upload.tpl', tag_lists = tag_list)


@route('/oauth_callback')
def on_callback():
    code = request.GET.get("code")
    if not code:
        return 'Missing code'
    try:
        access_token, user_info = unauthenticated_api.exchange_code_for_access_token(code)
        if not access_token:
            return 'Could not get access token'
        api = client.InstagramAPI(access_token=access_token, client_secret=CONFIG['client_secret'])
        request.session['access_token'] = access_token
    except Exception as e:
        print(e)
    return template('menu')



@route('/tag_search')
def on_tag_search():
    access_token = request.session['access_token']
    api = client.InstagramAPI(access_token=access_token, client_secret=CONFIG['client_secret'])

    bot = InstaManager(
        login="urbanshot__",
        password="kluza1",
        tag_list=['NieziemskieKaty', 'cute', 'sweet'],
        log_mod=0)

    if (int(bot.media_count) % 20) > 0:
        counter = (int(bot.media_count) / 20)
    else:
        counter = (int(bot.media_count) / 20) - 1

    media_id_before = api.user_recent_media(user_id="self")[0]
    media = []
    for i in media_id_before:
        media_id = str(i)
        media.append(media_id[7:])
    print(media)

    api.media_likes(media[1])


    ui_manager = UserInfo()
    ui_manager.followed_by_count = int(get_followed_by_count())

    time.sleep(30)

    followed_by_count = int(get_followed_by_count())
    print 'Followed by before: %d' % ui_manager.followed_by_count
    print 'Followed by after: %d' % followed_by_count

    if followed_by_count > ui_manager.followed_by_count:
        difference = followed_by_count - ui_manager.followed_by_count
        ui_manager.get_followed_by()
        while difference > 0:
            bot.follow(ui_manager.followed_by[difference-1]['id'])
            bot.unfollow(ui_manager.followed_by[difference - 1]['id'])
            difference -= 1

    return template('data',
                            posts= bot.media_count,
                            following=  get_follows_count(),
                            followed= get_followed_by_count()
                    )

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


bottle.run(app=app, host='localhost', port=8515, reloader=True)
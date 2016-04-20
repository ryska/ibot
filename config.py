from instagram import client

CONFIG = {
    'client_id': '7da4a6bf233f41ccb5f3e9a444217951',
    'client_secret': '512f10cd05524dce9a25a21d5fed181a',
    'redirect_uri': 'http://localhost:8515/oauth_callback'
}

unauthenticated_api = client.InstagramAPI(**CONFIG)

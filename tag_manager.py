import bottle
import beaker.middleware
import urllib
import requests
from collections import Counter
import pynstagram
import pic_manager
from pic_manager import cut_image, upload
from config import CONFIG
from bottle import route, redirect, post, run, request, hook, template
from instagram import client, subscriptions


def search_tag():
    access_token = request.session['access_token']
    familiar_tags = ["l4l","l4l","l4l","l4l","l4l","l4l","l4l","l4l","l4l","l4l",
                     "l4l", "l4l", "l4l", "l4l", "l4l", "l4l", "l4l", "l4l", "l4l", "l4l",
                     "l4l", "l4l", "l4l", "l4l", "l4l", "l4l", "l4l", "l4l", "l4l", "l4l",
                     "l4l", "l4l", "l4l", "l4l", "l4l", "l4l", "l4l", "l4l", "l4l", "l4l",
                     "l4l", "l4l", "l4l", "l4l", "l4l", "l4l", "l4l", "l4l", "l4l", "l4l",]
    #[{"#like4like",100}, {"#likeme",100}, {"#followme",100}]          #lista tagow, ktore sa w opisach znalezionych zdjec
    current_tag = "vsco"     #tag, po ktorym odbywa sie wyszukiwanie
    content = "<h2>Tag Search</h2>"
    if not access_token:
        return 'Missing Access Token'
    try:
        api = client.InstagramAPI(access_token=access_token, client_secret=CONFIG['client_secret'])
        tag_search, next_tag = api.tag_search(q=current_tag)
        tag_recent_media, next = api.tag_recent_media(tag_name=tag_search[0].name)
        photos = []
        for tag_media in tag_recent_media:
            photos.append('<img src="%s"/>' % tag_media.get_standard_resolution_url() )
            photos.append('</br>%s' % tag_media.caption.text )

            #petla wyszukujaca w opisie tagow i dodajaca je do listy
            for tag in get_tags(tag_media.caption.text):
                familiar_tags.append(tag)

        #Counter - funkcja zaimportowana z collections; tworzy krotki (element_listy, liczba_wystapien)
        familiar_tags = Counter(familiar_tags).most_common()
        content += ''.join(photos)
        content += "</br></br>Current tag: %s" % current_tag
        content += "</br>%s" % familiar_tags
        upload(familiar_tags)
    except Exception as e:
        print(e)
    return "%s %s <br/>Remaining API Calls = %s/%s" % (get_nav(), content, api.x_ratelimit_remaining, api.x_ratelimit)


def get_tags(caption):
    current_tag = ""
    tag_list = []
    tag_found = False

    for item in caption:
        if( item == '#' ):
            tag_found = True
            if (item == '#' and current_tag != ''):
                tag_list.append(current_tag)
                current_tag = ''

        elif( item != '#' and item != ' ' and tag_found == True):
            current_tag += item


        elif( item == ' ' and tag_found == True):
            tag_list.append(current_tag)
            current_tag = ""
            tag_found = False

    if( current_tag != "" and tag_found == True ):
        tag_list.append(current_tag)

    return tag_list

def get_nav():
    tag_url = '/tag_search'
    # nav_menu = ("<h1>Python Instagram</h1>"
    #             "<ul>"
    #                 "<li><a href='{{tag}}'>Tags</a> Search for tags, view tag info and get media by tag</li>"
    #                 #"<li><a href='/upload'>Upload</a> Upload pic</li>"
    #             "</ul>"
    #             )
    return template('nav_menu', tag = tag_url)
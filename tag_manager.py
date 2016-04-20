import bottle
import beaker.middleware
import urllib2
import requests
from collections import Counter
import pynstagram
import pic_manager
from six.moves import urllib
from urllib2 import request_host
from pic_manager import cut_image, upload
from config import CONFIG
from bottle import route, redirect, post, run, request, hook, template
from instagram import client, subscriptions



def search_tag():
    page = urllib.request.urlopen('http://websta.me/hot')
    content = page.read()
    splitted_content = content.split('<a href="/tag/', 100)
    tag_lists = []

    for tag_cell in splitted_content[1:]:
        splitted_tag = tag_cell.split('">#', 1)
        tag_lists.append(splitted_tag[0])
    return tag_lists


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

    return ''.join(tag_list)


# def get_nav():
#     tag_url = '/tag_search'
#     # nav_menu = ("<h1>Python Instagram</h1>"
#     #             "<ul>"
#     #                 "<li><a href='{{tag}}'>Tags</a> Search for tags, view tag info and get media by tag</li>"
#     #                 #"<li><a href='/upload'>Upload</a> Upload pic</li>"
#     #             "</ul>"
#     #             )
#     return template('nav_menu', tag = tag_url)
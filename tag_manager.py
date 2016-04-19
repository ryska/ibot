from bottle import template
from six.moves import urllib


def search_tag():
    page = urllib.request.urlopen('http://websta.me/hot')
    content = page.read()
    splitted_content = content.split('<a href="/tag/', 100)
    tag_lists = []

    for tag_cell in splitted_content[1:]:
        splitted_tag = tag_cell.split('">#', 1)
        tag_lists.append(splitted_tag[0])
    return tag_lists

def get_nav():
    tag_url = '/tag_search'
    # nav_menu = ("<h1>Python Instagram</h1>"
    #             "<ul>"
    #                 "<li><a href='{{tag}}'>Tags</a> Search for tags, view tag info and get media by tag</li>"
    #                 #"<li><a href='/upload'>Upload</a> Upload pic</li>"
    #             "</ul>"
    #             )
    return template('nav_menu', tag = tag_url)
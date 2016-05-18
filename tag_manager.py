#from six.moves import urllib
import urllib2


def search_tag():
    page = urllib2.urlopen('http://websta.me/hot')
    content = page.read()
    splitted_content = content.split('<a href="/tag/', 100)
    tag_lists = []

    for tag_cell in splitted_content[1:]:
        splitted_tag = tag_cell.split('">#', 1)
        tag_lists.append(splitted_tag[0])
    return tag_lists


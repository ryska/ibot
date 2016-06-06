import urllib
import pynstagram
import ssl
from PIL import Image
from database.database_manager import get_count_tag_by_category

def get_default_category_tags(list):
    list.extend(get_count_tag_by_category('Likes', 5))
    list.extend(get_count_tag_by_category('Comments', 5))
    list.extend(get_count_tag_by_category('Follow me', 5))
    list.extend(get_count_tag_by_category('Shoutout', 5))
    return list

def get_tags(category, limit):
    list = []
    list.extend(get_count_tag_by_category(category, limit))
    get_default_category_tags(list)
    return list

def urban_url():
    return "buildings"


def upload(list):
    #list = get_tags(category)
    context = ssl._create_unverified_context()
    #category_url = get_category_url(category)
    urllib.urlretrieve("https://source.unsplash.com/category/"+"buildings"+"/1400x1200", "pic1.jpg", context=context)
    cut_image()
    with pynstagram.client('urbanshot__', 'kluza1') as client:
        tags = ''
        for tag in list:
            tags = tags + '#' + tag + ' '
        client.upload('pic1.jpg', tags)
    return list

def cut_image():
    img = Image.open("pic1.jpg")
    half_width = img.size[0] / 2
    half_height = img.size[1] / 2
    img1 = img.crop(
        (
            half_width - 450,
            half_height - 450,
            half_width + 450,
            half_height + 450
        )
    )
    img1.save("pic1.jpg")
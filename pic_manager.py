import urllib
import pynstagram
from PIL import Image

def upload(search_tag):
    list = search_tag()
    urllib.urlretrieve("https://source.unsplash.com/category/buildings/1400x1200", "pic1.jpg")
    cut_image()
    with pynstagram.client('urbanshot__', 'kluza1') as client:
        tags = ''
        for i in range(15):
            tags = tags + '#' + list[i] + ' '
        client.upload('pic1.jpg', tags)

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
import urllib
import pynstagram
from PIL import Image

def upload(list):
    urllib.urlretrieve("https://source.unsplash.com/category/buildings/1400x1200", "pic1.jpg")
    cut_image()
    with pynstagram.client('urbanshot__', 'kluza1') as client:
        client.upload('pic1.jpg', '#'+list[0][0]+' #'+list[1][0])
    #return "<p>Uploaded!</p>"

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
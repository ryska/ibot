import urllib
import pynstagram
import ssl
from PIL import Image
from database.database_manager import DatabaseManager

class PicManager:
    def __init__(self):
        self.data_manager = DatabaseManager()
        self.pic_site = "https://source.unsplash.com/category/"
        self.pic_size = "/1400x1200"
        self.pic_to_upload = "pic1.jpg"

    # zwraca liste 20 defaultowych tagow LIKE COMENT FOLLOW SHOUTOUT
    def get_default_category_tags(self, list):
        list.extend(self.data_manager.get_count_tag_by_category('Likes', 5))
        list.extend(self.data_manager.get_count_tag_by_category('Comments', 5))
        list.extend(self.data_manager.get_count_tag_by_category('Follow me', 5))
        list.extend(self.data_manager.get_count_tag_by_category('Shoutout', 5))
        return list

    # zwraca liste tagow z zadanej kategorii
    # 20 tagow defaultowych i okreslone parametrem limit tagi z zadanej kategorii
    def get_tags(self, category, limit):
        list = []
        list.extend(self.data_manager.get_count_tag_by_category(category, limit))
        self.get_default_category_tags(list)
        return list

    def urban_url(self):
        return "buildings"

    # dodaje zdjecie
    def upload(self, list):
        list = self.get_tags("Urban", 10)
        context = ssl._create_unverified_context()
        #category_url = get_category_url(category)
        urllib.urlretrieve(self.pic_site + "buildings" + self.pic_size, self.pic_to_upload, context=context)
        self.cut_image()
        with pynstagram.client('urbanshot__', 'kluza1') as client:
            tags = ''
            for tag in list:
                tags = tags + '#' + tag + ' '
            client.upload('pic1.jpg', tags)
        return list

    # przycina zdjecie do kwadratu
    def cut_image(self):
        img = Image.open(self.pic_to_upload)
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
        img1.save(self.pic_to_upload)
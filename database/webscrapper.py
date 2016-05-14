from six.moves import urllib

# ZWRACA STRINGA - TRESC STRONY
def read_content():
    page = urllib.request.urlopen('http://www.tagblender.net')
    content = page.read()
    return content

# ROZDZIELENIE NA KATEGORIE
def category_split(content):
    splitted_content = content.split('<div class="categoryContainer">', 24)
    splitted_content.pop(0)
    splitted_content[23] = splitted_content[23][0:-400]
    return splitted_content

# ROZDZIELENIE NA PODKATEGORIE
def subcategory_split(category):
    splitted_content2 = category.split('<h2>', 6)
    splitted_content2.pop(0)
    return splitted_content2

# ROZDZIELENIE TYTULU
def title_split(subcategory):
    splitted_content = subcategory.split('</h2>', 1)
    splitted_content2 = splitted_content[0].split(' <span', 1)
    category_title = splitted_content2[0]
    if category_title.startswith('+'):
        category_title = category_title[1:]
    return category_title

# ROZDZIELENIE HASHTAGU
def hashtags_split(subcategory):
    splitted_content3 = subcategory.split('</h2>', 1)
    splitted_content4 = splitted_content3[1].split('#', 1)
    splitted_content4.pop(0)
    splitted_content5 = splitted_content4[0].split('\t', 1)
    hashtags = splitted_content5[0].split(' #', 30)
    return hashtags

import sqlite3;
from webscrapper import category_split, subcategory_split, title_split, hashtags_split, read_content

con = sqlite3.connect('tag_database.db')
#con.row_factory = lambda cursor, row: row[0]
con.text_factory = str
con.row_factory = sqlite3.Row
cur = con.cursor()

# nie odpalac
#usuwa tabele
def delete_tags_table():
    cur.execute("DROP TABLE IF EXISTS Tags;")
    con.commit()

# nie odpalac, chociaz mozna bo wywali blad
#tworzy tabele tagow
def create_tags_tables():
    cur.execute("""
         CREATE TABLE IF NOT EXISTS Tags (
        tag varchar(50) NOT NULL,
        category varchar(50) NOT NULL,
        PRIMARY KEY (tag,category)
        )""")
    con.commit()

#wstawia wiersz do tabeli
def insert_value(tag, category):
    cur.execute(
        "INSERT OR IGNORE INTO Tags (tag, category) VALUES (?,?)",(tag,category,))
    con.commit()

#zwraca liste tagow z zadanej kategorii
def get_tag_by_category(category):
    cur.execute("select tag from Tags where category=? ORDER BY random()",(category,))
    ar = [str(item[0]) for item in cur.fetchall()]
    return ar

#zwraca liste tagow o zadanej dlugosci i zadanej kategorii
def get_count_tag_by_category(category, count):
    cur.execute("select tag from Tags where category=? ORDER BY random() limit ?",(category,count))
    ar = [str(item[0]) for item in cur.fetchall()]
    return ar

#zwraca liste kategorii
def get_categories():
    cur.execute("select distinct category from Tags ")
    ar = [str(item[0]) for item in cur.fetchall()]
    return ar


#nie odpalac :D
#wypelnia baze danych naszymi danymi
def fill_database():
    categories = category_split(read_content())
    for cat in categories:
        for sub in subcategory_split(cat):
            category = title_split(sub)
            for tag in hashtags_split(sub):
                insert_value(tag,category)

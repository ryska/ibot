import sqlite3;
from webscrapper import category_split, subcategory_split, title_split, hashtags_split, read_content

con = sqlite3.connect('tag_database.db')
con.text_factory = str
con.row_factory = sqlite3.Row
cur = con.cursor()

# nie odpalać
#usuwa tabele
def delete_tags_table():
    cur.execute("DROP TABLE IF EXISTS Tags;")
    con.commit()

# nie odpalać, chociaż można bo wywali bląd
#tworzy tabele tagow
def create_tags_table():
    delete_tags_table()
    cur.execute("""
         CREATE TABLE IF NOT EXISTS Tags (
        tag varchar(50) NOT NULL,
        category varchar(250) NOT NULL
        )""")
    con.commit()

#wstawia wiersz do tabeli
def insert_value(tag, category):
    cur.execute(
        "INSERT INTO Tags (tag, category) VALUES (?,?)",(tag,category,))
    con.commit()

#zwraca liste tagow z zadanej kategorii
def get_tag_by_category(category):
    cur.execute("select tag from Tags where category=?",(category,))
    return cur.fetchall()

#zwraca liste tagow o zadanej dlugosci i zadanej kategorii
def get_count_tag_by_category(category, count):
    cur.execute("select tag from Tags where category=? limit ?",(category,count,))
    return cur.fetchall()

#wyswietla tabele
def show_database():
    cur.execute("select * from tags")
    return cur.fetchall()

#nie odpalać :D
#wypelnia baze danych naszymi danymi
def fill_database():
    categories = category_split(read_content())
    for cat in categories:
        for sub in subcategory_split(cat):
            category = title_split(sub)
            for tag in hashtags_split(sub):
                insert_value(tag,category)

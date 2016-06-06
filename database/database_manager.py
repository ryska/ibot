import sqlite3;
from webscrapper import category_split, subcategory_split, title_split, hashtags_split, read_content


class DatabaseManager:

    # inicjalizuje połączenie z tabelą
    def __init__(self):
        self.con = sqlite3.connect('tag_database.db')
        self.con.text_factory = str
        self.con.row_factory = sqlite3.Row
        self.cur = self.con.cursor()

    # usuwa tabele tags z bazy
    def delete_tags_table(self):
        self.cur.execute("DROP TABLE IF EXISTS Tags;")
        self.con.commit()

    # tworzy tabele jeśli nie istnieje
    def create_tags_tables(self):
        self.cur.execute("""
          CREATE TABLE IF NOT EXISTS Tags (
          tag varchar(50) NOT NULL,
          category varchar(50) NOT NULL,
          PRIMARY KEY (tag,category)
          )""")
        self.con.commit()

    # wstawia wiersz do tabeli
    def insert_value(self, tag, category):
        self.cur.execute(
            "INSERT OR IGNORE INTO Tags (tag, category) VALUES (?,?)",(tag,category,))
        self.con.commit()

    # zwraca liste tagow z zadanej kategorii
    def get_tag_by_category(self, category):
        self.cur.execute("select tag from Tags where category=? ORDER BY random()",(category,))
        ar = [str(item[0]) for item in self.cur.fetchall()]
        return ar

    # zwraca liste tagow o zadanej dlugosci i zadanej kategorii
    def get_count_tag_by_category(self, category, count):
        self.cur.execute("select tag from Tags where category=? ORDER BY random() limit ?",(category,count))
        ar = [str(item[0]) for item in self.cur.fetchall()]
        return ar

    # zwraca liste kategorii
    def get_categories(self):
        self.cur.execute("select distinct category from Tags ")
        ar = [str(item[0]) for item in self.cur.fetchall()]
        return ar


    # wypelnia baze danych naszymi danymi
    def fill_database(self):
        categories = category_split(read_content())
        for cat in categories:
            for sub in subcategory_split(cat):
                category = title_split(sub)
                for tag in hashtags_split(sub):
                    self.insert_value(tag,category)


    def scrap(self):
        self.delete_tags_table()
        self.create_tags_tables()
        self.fill_database()

import sqlite3;

con = sqlite3.connect('tag_database.db')
con.row_factory = sqlite3.Row
cur = con.cursor()

#usuwa tabele
def delete_tags_table():
    cur.execute("DROP TABLE IF EXISTS Tags;")
    con.commit()

#tworzy tabele tagow
def create_tags_table():
    delete_tags_table()
    cur.execute("""
         CREATE TABLE IF NOT EXISTS Tags (
        tag varchar(50) PRIMARY KEY,
        popularity INTEGER,
        category varchar(250) NOT NULL
        )""")
    con.commit()

#wstawia wiersz do tabeli
def insert_value(tag, popularity, category):
    cur.execute(
        "INSERT INTO Tags (tag, popularity, category) VALUES (?,?,?)",(tag,popularity,category,))
    con.commit()

#zwraca liste tagow z zadanej kategorii
def get_tag_by_category(category):
    cur.execute("select tag from Tags where category=?",(category,))
    return cur.fetchall()

#zwraca liste tagow o zadanej dlugosci i zadanej kategorii
def get_count_tag_by_category(category, count):
    cur.execute("select tag from Tags where category=? limit ?",(category,count,))
    return cur.fetchall()

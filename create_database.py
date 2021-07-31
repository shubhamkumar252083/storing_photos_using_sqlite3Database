
import sqlite3
open("pic_data.db", "w").close()
sqliteConnection = sqlite3.connect('pic_data.db')
cursor = sqliteConnection.cursor()
cursor.execute(
    "CREATE TABLE pic ( id INTEGER PRIMARY KEY, photo BLOB NOT NULL)")
print("CREATED SQLite DATABASE")

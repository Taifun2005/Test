import sqlite3
import random

from numpy.random.mtrand import random

connection = sqlite3.connect("database.db")
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER
)
''')

cursor.execute(" CREATE INDEX IF NOT EXISTS idx_email ON Users (email)")

# cursor.execute(" INSERT INTO Users (username, email, age) VALUES (?, ?, ?)",("newuser", "ex@gmail.com", "28"))
for i in range(20):
    cursor.execute(" INSERT INTO Users (username, email, age) VALUES (?, ?, ?)", (f"newuser{i}", f"{i}ex@gmail.com", str(random.randint(1,49))))
# cursor.execute("UPDATE Users SET age = ? WHERE username = ?", (29,"newuser"))
# cursor.execute("DELETE FROM Users WHERE username = ?", ("newuser3",))

connection.commit()
connection.close()
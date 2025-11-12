import sqlite3
con = sqlite3.connect("tutorial.db")
cur = con.cursor()
#cur.execute("CREATE TABLE movie(title, year, score)")
result = cur.execute("select * from movie")
print (result.fetchone())

sql = """
    INSERT INTO movie VALUES
        ('Monty Python and the Holy Grail', 1975, 8.2),
        ('And Now for Something Completely Different', 1971, 7.5)
"""
# DANGER DANGER this can lead to SQL injection
cur.execute(sql)



result = cur.execute("select * from movie")
print (result.fetchone())

data = [
    ("Monty Python's Life of Brian", 1979, 8.0),
]
cur.executemany("INSERT INTO movie VALUES(?, ?, ?)", data)
con.commit()  # Remember to commit the transaction after executing INSERT.


for row in cur.execute("select * from movie"):
    print (f"row{row}")

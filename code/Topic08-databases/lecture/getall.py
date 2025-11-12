import sqlite3
con = sqlite3.connect("lecture.db")
cur = con.cursor()

sql = "select * from student where gender = 'Female'"
result = cur.execute(sql)
for row in result.fetchall():
    print(row)
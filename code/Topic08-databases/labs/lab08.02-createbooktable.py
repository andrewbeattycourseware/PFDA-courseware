import sqlite3
con = sqlite3.connect("pfda.db") # I will call this database pdfa.db
cur = con.cursor()
#sql = "DROP TABLE IF EXISTS book"
#cur.execute(sql)

cur.execute("CREATE TABLE book(title, author, ISBN)")
# no errors? we should write some code to test this exists
# or even a print to say "done"
con.close()
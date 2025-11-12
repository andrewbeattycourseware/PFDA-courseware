import mysql.connector

db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
 database="pfda"
)

cursor = db.cursor()
sql="update student set name= %s, age=%s  where id = %s"
values = ("Joe",33, 1)

cursor.execute(sql, values)

db.commit()
print("update done")

cursor.close()
db.close()

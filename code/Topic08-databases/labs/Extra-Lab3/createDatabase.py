import mysql.connector

db = mysql.connector.connect(
  host="localhost",
  user="root",
  password=""
)

cursor = db.cursor()

cursor.execute("create DATABASE pfda")

db.close()
cursor.close()
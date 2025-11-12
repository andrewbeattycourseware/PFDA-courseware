import mysql.connector

db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="pfda"
)

cursor = db.cursor()
sql="CREATE TABLE student (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(250), age INT)"

cursor.execute(sql)

db.close()
cursor.close()
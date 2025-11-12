import mysql.connector
class StudentDAO:
    host =""
    user = ""
    password =""
    database =""

    connection = ""
    cursor =""

    def __init__(self): 
        #these should be read from a config file
        self.host="localhost"
        self.user="root"
        self.password=""
        self.database="pfda"
    
    def getCursor(self): 
        self.connection = mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database
        )
        self.cursor = self.connection.cursor()
        return self.cursor
    
    def closeAll(self):
        self.connection.close()
        self.cursor.close()
    
    
    def getAll(self):
        cursor = self.getCursor()
        sql="select * from student"
        cursor.execute(sql)
        result = cursor.fetchall()
        studentlist = []
        for row in result:
            studentlist.append(self.convertToDict(row))

        self.closeAll()
        return studentlist

    def findByID(self, id):
        cursor = self.getCursor()
        sql="select * from student where id = %s"
        values = (id,)

        cursor.execute(sql, values)
        result = cursor.fetchone()
        self.closeAll()
        return self.convertToDict(result)
    
    def create(self, student):
        cursor = self.getCursor()
        sql="insert into student (name, age) values (%s,%s)"
        values = (student.get("name"), student.get("age"))
        cursor.execute(sql, values )

        self.connection.commit()
        newid = cursor.lastrowid
        student["id"] = newid
        self.closeAll()
        return student


    def update(self, id,  student):
        cursor = self.getCursor()
        sql="update student set name= %s, age=%s  where id = %s"
    
        values = (student.get("name"), student.get("age"), id)
        cursor.execute(sql, values)
        self.connection.commit()
        
        self.closeAll()
        return student

    def delete(self, id):
        cursor = self.getCursor()
        sql="delete from student where id = %s"
        values = (id,)

        cursor.execute(sql, values)

        self.connection.commit()
        self.closeAll
        #print("delete done")
        return True

    def convertToDict(self,resultLine):
        studentKeys = ["id", "name", "age"]
        currentkey = 0
        student = {}
        for attrib in resultLine:
            student[studentKeys[currentkey]] = attrib
            currentkey = currentkey + 1 
        return student

studentDAO = StudentDAO()
from zstudentDAO import studentDAO


student = {
  "name":"mark", 
  "age":31
  }
#create
student = studentDAO.create(student)
studentid = student["id"]
# find by id
result = studentDAO.findByID(studentid);
print ("test create and find by id")
print (result)

#update
newstudentvalues= {"name":"fred", "age":18}
studentDAO.update(studentid,newstudentvalues)
result = studentDAO.findByID(studentid);
print("test update")
print (result)

# get all 
print("test get all")
allStudents = studentDAO.getAll()
for student in allStudents:
  print(student)

# delete
studentDAO.delete(studentid)


#File Handling:

#A school wants to maintain student records using a text file.
 
#You are required to write a Python program that performs the following file handling operations step by step:
 
#1) Write Operation:

#- Create a file named students.txt.

#- Write details of students (Name, Roll Number, Marks) into the file.
 
#2) Read Operation:

#- Read the content of students.txt and display it on the screen.
 
#3) Rename Operation:

#- Rename the file from students.txt to student_records.txt.
 
#4) Directory Operations:

#- Create a directory called SchoolData.

#- Move the renamed file student_records.txt into this directory.

#- List all files present in SchoolData to confirm the file is inside.
 
#5) Delete Operation:

#- Delete the file student_records.txt from inside the directory.
 
#Finally, delete the SchoolData directory.
    
#Do create a menu taking the user input and then perform the operation

import os

# Create a file to store student into a text file 

schoolfile = None

students = [{
    "name": "Student1",
    "Roll": 1,
    "Marks": 30
},
{
    "name": "Student2",
    "Roll": 2,
    "Marks": 50
},
{
    "name": "Student3",
    "Roll": 30,
    "Marks": 80
}
]

try:
    #create a school file
    schoolfile = open('./Assignment/students.txt', 'w')
    for student in students:
        schoolfile.write(f"{student['name']} {student['Roll']} {student['Marks']}\n")
    print("Students data written to file successfuly")
    schoolfile.close()
    # Read the school file and print
    schoolfile = open('./Assignment/students.txt', 'r')
    while True:
        student = schoolfile.readline().split()
        if not student:
            break
        print(f"Name: {student[0]} Roll: {student[1]} Marks: {student[2]}")
    schoolfile.close()
    #Rename the file.
    os.rename('./Assignment/students.txt', './Assignment/student_records.txt')
    print("File renamed successfuly")

    # create a directory
    os.mkdir('./Assignment/SchoolData')
    print ("Directory Created successfuly")

    # Move file to the directory
    os.replace('./Assignment/student_records.txt', './Assignment/SchoolData/student_records.txt')
    
    #List all the file in the directory
    listoffiles = os.listdir('./Assignment/SchoolData')
    print (listoffiles)

    #Remove the file
    path = './Assignment/SchoolData/'
    for file in listoffiles:
        os.remove(path + file)
    print("File deleted successfully")

    #remove directory
    os.rmdir(path)
    print("Removed directory successfully")
    
except Exception as e:
    print(f"Exception occured {e}")
 
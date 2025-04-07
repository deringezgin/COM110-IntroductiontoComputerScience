#module to create a Registrar Class
#imports the Student class from module StudentClass.py

from studentClass import *

class Registrar:
    """class Registrar has the following instance variables:
        studentList is a list of Student objects
        totStudents is an integer that counts the total number of students"""

    def __init__(self):
        """constructor sets up a blank registrar"""
        self.studentList=[] 
        self.totStudents=0;
        
    def addStudent(self, stu):
        """add a new student (Student object stu) to the Registrar"""
        self.studentList.append(stu)
        self.totStudents = self.totStudents + 1

    def deleteStudent(self, stu):
        """delete a student (Student object stu) from the list"""        
        for student in self.studentList:
            if student==stu:
                self.studentList.remove(stu)
                self.totStudents = self.totStudents - 1

    def printInfo(self):
        """print out the information for all students"""
        print ('++++++++++++++')
        print ("There are " + str(self.totStudents) + " students currently registered." )
        for student in self.studentList:
            student.printInfo()
        print ('++++++++++++++')


    def registerCourse(self, stuID, courseName, studentobj): # Creating the registerCourse method
        studentobj.courseList.append(courseName)

#Test out our registrar class
def main():

    #create two students
    student1 = Student("Jones", 23423, ["COM110","BIO101", "PSY101"])
    student2 = Student("Gonzalez", 65234)

    student1.printInfo() # Printing before adding a new course
    reg1 = Registrar() # Creating a Registrar Object
    reg1.registerCourse(student1.id, "STA107", student1) # Calling the method from the class
    student1.printInfo() # Printing after adding a new course to check

main()




"""
### MY ANSWERS FOR THE QUESTIONS ###

# Which lines of code create new Student objects?

In registrar.py lines 44 and 45 creates new student objects. 
    (line 44) student1 = Student("Jones", 23423, ["COM110","BIO101", "PSY101"])
    (line 45) student2 = Student("Gonzalez", 65234)

In studentClass.py lines 41 and 45 creates new student objects.
    (line 41) stu1=Student('Jones',89765,['COM110', 'HIS112','DAN100'])
    (line 45) stu2=Student('Gonzalez',65432)

# What are the instance variables of the Student class?  And the methods?

    Instance Variables:
        - name
        - id
        - courseList

    Methods:
        - __init__
        - setCourseList
        - addCourse
        - printInfo
        - changeName
"""





























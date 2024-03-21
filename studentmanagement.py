# Problem Statement: Write a program to build a simple Student Management System using Python which can perform the following operations:

# Accept
# Display
# Search
# Delete
# Update

class Student:
    def __init__(self,name,rollno,m1,m2):
        self.name=name
        self.rollno=rollno
        self.m1=m1
        self.m2=m2

    def accept(self,Name,Rollno,marks1,marks2):
        ob = Student(Name,Rollno,marks1,marks2)
        ls.append(ob)
    def display(self,ob):
        print("Name   : ", ob.name)
        print("Marks1 : ", ob.m1)
        print("Marks2 : ", ob.m2)
        print("RollNo : ", ob.rollno)
        print("\n")    
    def search(self,rn):
        for i in range(len(ls)):
            if(ls[i].rollno == rn):
                return i 
    def delete(self,student_no):
    
        del ls[student_no]
        
    def update(self,rn,No):
        i =obj.search(rn)
        ls[i].rollno= No
    
ls =[]
obj =Student('',0,0,0)

ch = 0
print("\nOperations used, ")
print("\n1.Accept Student details\n2.Display Student Details\n3.Search Details of a Student\n4.Delete Details of Student\n5.Update Student Details\n6.Exit")
while ch != 6:
    ch=int(input('Enter Choice'))
    if (ch==1):
        print('Enter Students details  ')
        name=input('Enter name')
        ##Roll Number of Each Student must be unique
        while True:
            rollno=int(input('Enter roll no'))
            if obj.search(rollno)== None:
                break
            else:
                print('Entered Roll Number Already Exist')

        marks1=int(input('Enter marks1'))
        marks2=int(input('Enter marks2'))
        obj.accept(name,rollno,marks1,marks2)
    elif(ch==2):
        rollno=int(input('Enter rollno of student '))
        result =obj.search(rollno)  
        if(result==None):
            print('Student with entered roll no ',rollno,' doesnot exist')
        else:
            obj.display(ls[obj.search(rollno)])
    elif(ch==3):
        rollno=int(input('Enter rollno of student '))
        
        obj.search(rollno)
    elif(ch==4):

        rollno=int(input('Enter rollno of student '))
        result =obj.search(rollno)  
        if(result==None):
            print('Student with entered roll no ',rollno,' doesnot exist')
        else:
            obj.delete(result)
    elif ch==5:

        rollno=int(input('Enter rollno of student '))
        result =obj.search(rollno)  
        if(result==None):
            print('Student with entered roll no ',rollno,' doesnot exist')
        else:
            newrollno=int(input('Enter newrollno of student '))
            obj.update(rollno,newrollno)
        
        
    









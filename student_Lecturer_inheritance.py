# Creating a parent class student
class Student:
    # Intialization of variables
    def __init__(self,name,age,RegNo,AccessNumber,Course):
        self.name=name
        self.age=age
        self.RegNo=RegNo
        self.AccessNumber=AccessNumber
        self.Course=Course
    # Using the show_info function to output the Student's information from the Construtor ,, Alternatively you can use  the __Str_ and the __Repr__ functions to get the
    def show_info(self):
        print("Student Information")
        print("Name: ",self.name)
        print("Age: ",self.age)
        print("RegNo: ",self.RegNo)
        print("AccessNumber: ",self.AccessNumber)
        print("Course: ",self.Course)    
    #Creating the Lecturer class and this will inherit from the students
    # The Lecturer class for this case will act as the Child class and this will inherit the similar attributes from the Student parent class
class Lecturer(Student):
    # First create the Lecturer constructor and initialize the Attributes 
    def __init__(self,name,age,RegNo,AccessNumber,Course,salary,department):
        # Use the Super() method to create inherit the Rest of the Data from the Parent class
        super().__init__(name,age,RegNo,AccessNumber,Course)
        # Initializing the Additional attributes 
        self.salary=salary
        self.department=department
    #  Create a function that will return the data for the given department lecturer    
    def show_info(self):
        print("Lecturer.Information")
        super().show_info()
        print("Salary: ",self.salary)
        print("Department: ",self.department)
    
    
        #Create the main class and this function will help you organize the Objects 
def  main():
    student1=Student("John Muwonge",20,"J22B12345","A2345","Computer Science")
    lecturer1=Lecturer("Luke Musoke",21,"L123","A9763","Computer Science",50000,"Computing and Technology")
    lecturer1.show_info()
    student1.show_info()   
main()

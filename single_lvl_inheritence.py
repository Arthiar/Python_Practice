"""#Getting input from the user
# Single level inheritance

# Parent class
class Animal:
    def __init__(self, a_name):
        self.a_name = a_name

    def name(self):
        print(f"{self.a_name} makes a sound.")

# Child class (inherits from Animal)
class Dog(Animal):
    def __init__(self, a_name, name, breed):
        super().__init__(a_name)   # call parent constructor
        self.breed = breed
        self.names = name

    def category(self):
        print(f"{self.names} barks! (Breed: {self.breed} and it's an {self.a_name})")


# ---------------- MAIN PROGRAM ----------------

# Take input from user
a_name = input("Enter the type of animal (e.g., Europe breed): ")
name = input("Enter the dog's name: ")
breed = input("Enter the dog's breed: ")

# Create object with user input
d = Dog(a_name, name, breed)

# Use methods
d.category()
d.name()"""

#######################################################################################################
#student id programm getting input 

class Student: #parent class
    def __init__(self,name,age):
        self.name= name
        self.age=age
        
class Identity(Student): #child class
    def __init__(self,name,age,idty,grade):
        super().__init__(name,age)
        self.idty= idty
        self.grade=grade
    def personal(self):
        print(f"{self.name} is {self.age} years old and Has an id {self.idty}and is in {self.grade}")

#To get multiple inputs        
students = []  # empty list to store multiple Identity objects

n = int(input("How many students do you want to enter? "))

#Taking input from user
for r in range(n):
   name=input("Enter the user name: ")
   age=int(input("Enter the user age: "))
   idty=input("Enter the user`s id: ")
   grade=input("Enter the user grade: ")

#creating object

i = Identity(name, age, idty, grade)
students.append(i) # create many students and append to list as students class has the memory for the list

for s in students:
    s.personal()




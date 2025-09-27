#Single level inheritence 
 
# Parent class
class Animal:
    def __init__(self, a_name):
        self.a_name = a_name

    def name(self):
        print(f"{self.a_name} makes a sound.")

class Dog(Animal):# Child class (inherits from Animal)
    def __init__(self,a_name, name, breed):
        
        super().__init__(a_name)   # call parent constructor
        self.breed = breed
        self.names = name

    def category(self):
        print(f"{self.names} barks! (Breed: {self.breed} and its an {self.a_name})")


# Create objects
d = Dog("Europe breed","Tommy", "Labrador")

# Use methods
d.category()
d.name()

################################################################################################################
# Parent class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    """def introduce(self):
        print(f"Hi, my name is {self.name} and I am {self.age} years old.")"""

# Child class
class Student(Person):
    def __init__(self, name, age, student_id, grade):# Call parent __init__ to set name and age
        super().__init__(name, age)
        self.student_id = student_id
        self.grade = grade

    
    def show_details(self): # New method just for Student
        print(f"Hi, my name is {self.name} and I am {self.age} years old and my Student ID: {self.student_id}, Grade: {self.grade}")


s1 = Student("Arthi", 21, "S1234", "A+")
s2= Student("Aravind",27,"S3456","A")
# Call parent class method
"""s1.introduce()
s2.introduce()"""
# Call child class method
s1.show_details()
s2.show_details()

#Multiple
class Father:
    def skills(self):
        print("Father: Knows driving")

class Mother:
    def skills(self):
        print("Mother: Knows cooking")

class Child(Father, Mother):   # inherits from BOTH
    def own_skill(self):
        print("Child: Knows painting")

c = Child()
c.skills()       # will take from Father first (left-to-right)
c.own_skill()
print("---------------------------------------------------------------------------------------------------")
#EG 2
# Parent 1
class Father:
    def __init__(self, father_name):
        self.father_name = father_name
# Parent 2
class Mother:
    def __init__(self, mother_name):
        self.mother_name = mother_name
# Child inherits from BOTH
class Child(Father, Mother):
    def __init__(self, father_name, mother_name, child_name):
        Father.__init__(self, father_name)   # init Father
        Mother.__init__(self, mother_name)   # init Mother
        self.child_name = child_name
    def show_family(self):#Method for child
        print(f"I am {self.child_name}, my father is {self.father_name}, and my mother is {self.mother_name}.")
# Create child object
c = Child("Rajamanickam", "Saraswathi", "Arthisree")
c.show_family()
print("---------------------------------------------------------------------------------------------------")

###########################################################################################################################
#Multilevel 

class Grandparent:
    def quality(self):
        print("Grandparent: Wise")

class Parent(Grandparent):#Parent inherit from grandparent
    def quality_p(self):
        print("Parent: Responsible")

class Child(Parent): #Child inherit from Parent
    def own_quality(self):
        print("Child: Energetic")

c = Child()
c.quality()
c.quality_p()      # comes from Parent
c.own_quality()
print("---------------------------------------------------------------------------------------------------")

#Eg:2
# Grandparent
class Grandparent:
    def __init__(self, grandparent_name):
        self.grandparent_name = grandparent_name
# Parent inherits from Grandparent
class Parent(Grandparent):
    def __init__(self, grandparent_name, parent_name):
        super().__init__(grandparent_name)   # call Grandparent init
        self.parent_name = parent_name
# Child inherits from Parent (multilevel)
class Child(Parent):
    def __init__(self, grandparent_name, parent_name, child_name):
        super().__init__(grandparent_name, parent_name)  # call Parent init
        self.child_name = child_name
    def show_family(self):#Child method
        print(f"I am {self.child_name}, my parent is {self.parent_name}, and my grandparent is {self.grandparent_name}.")
c = Child("Sreeranga Gounder", "Rajamanickam", "Arthisree") # Create only child object
c.show_family()
print("---------------------------------------------------------------------------------------------------")


##############################################################################################################
#Getting input 
# ---------------- MULTIPLE INHERITANCE ----------------
class Father:
    def __init__(self, house):
        self.house = house

class Mother:
    def __init__(self, shop):
        self.shop =  shop

class Child(Father, Mother):  # inherits from Father + Mother
    def __init__(self, house,shop,name, factory):
        Father.__init__(self, house)
        Mother.__init__(self, shop)
        self.name= name
        self.factory = factory

    def show_family(self):
        print(f"[Multiple] I am {self.name} and i own a {self.factory}, from my father I got his {self.house}, and from my mother I inherited her{self.shop}.")

# ---------------- MAIN PROGRAM ----------------
print("=== Multiple Inheritance ===")
children_multiple = [] #Creating a list to allocate memory and appending the looping values here
#For multiple inputs
n = int(input("How many children do you want to enter? "))
for r in range(n):  # looping
    print(f"\n--- Entering details for child {r+1} ---")
    house = input("Enter father's house name: ")
    shop = input("Enter mother's shop name: ")
    name = input("Enter child's name: ")
    factory = input("Enter the property child owns: ")

    c = Child(house, shop, name, factory)
    children_multiple.append(c)

print("\n--- Multiple Inheritance Families ---")
for c in children_multiple:
    c.show_family()
print("---------------------------------------------------------------------------------------------------")
# ---------------- MULTILEVEL INHERITANCE ----------------
class Grandparent:
    def __init__(self, car):
        self.car = car

class Parent(Grandparent):  # inherits from Grandparent so we use super insted of class name 
    def __init__(self, car, property):
        super().__init__(car) #we use super only for multilevel inheritence as we derive everything from the previous classes
        self.property = property

class Child1(Parent):  # inherits from Parent (multilevel)
    def __init__(self, car, property, my_name,my_age):
        super().__init__(car, property)
        self.my_name = my_name
        self.my_age = my_age

    def show_family(self):
        print(f"[Multilevel] I am {self.my_name}and I am {self.my_age} years old, I inherited {self.property}from my parents, and my grandparent had a  {self.car} which I got!.")

# MULTILEVEL INHERITANCE CASE
print("\n=== Multilevel Inheritance ===")

c_multilevel = [] #creatng the memory space 
n2 = int(input("How many children do you want to enter? "))

for r in range(n2):
    child_name = input(f"Enter name of child {r+1}: ")
    car = input("Enter grandparent's property that you inherit: ")
    property = input("Enter parent's property that u inherit: ")
    my_name= input("Enter your name: ")
    my_age = int(input("Enter your age please!= "))
    
    c1 = Child1(car, property, my_name, my_age)
    c_multilevel.append(c1)

print("\n--- Multilevel Inheritance Families ---")
for c in c_multilevel:
    c.show_family()

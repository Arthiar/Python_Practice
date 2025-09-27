# Parent class
class Person:
    def __init__(self, name):
        self.name = name

    def show_name(self):
        print(f"Name: {self.name}")


# Child 1 (inherits from Person)
class Student(Person):
    def __init__(self, name, grade):
        Person.__init__(self, name)   # direct call (avoid super here)
        self.grade = grade

    def show_grade(self):
        print(f"{self.name} is a Student with grade: {self.grade}")


# Child 2 (inherits from Person)
class Employee(Person):
    def __init__(self, name, job):
        Person.__init__(self, name)   # direct call
        self.job = job

    def show_job(self):
        print(f"{self.name} is an Employee working as: {self.job}")


# Hybrid child (inherits from Student + Employee)
class WorkingStudent(Student, Employee):
    def __init__(self, name, grade, job):
        Student.__init__(self, name, grade)   # initialize Student
        Employee.__init__(self, name, job)    # initialize Employee

    def show_details(self):
        print(f"{self.name} is a WorkingStudent with grade: {self.grade} and job: {self.job}")


print("Lets try printing multiple outputs")

worK_stu = []
n = int(input("Enter the no of entries: "))

for r in range(n):
    print(f"\n--- Enter the name of Person {r+1} ----")
    name = input("Enter your name: ")
    grade = input("How would you grade your work [Excellent, great, good, ok, negative]: ")
    job = input("Enter the name of the field you work in: ")

    c1 = WorkingStudent(name, grade, job)
    worK_stu.append(c1)

# Now print details OUTSIDE the loop
print("\n--- All Working Students ---")
for w in worK_stu:
    w.show_details()

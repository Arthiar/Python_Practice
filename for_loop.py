#hard_coding
names=["Arthi","Aravind", "Abhi", "Ajee","Lea","Kevin"]

for n in names:
    print(n.upper())
    print(n.lower())
    print(n.title())

#getting_input    
name=[]
n= int(input("Enter how many names: "))

for i in range(n):
    list=input (f"Enter the names{1+i}: ")
    name.append(list.title())
print("Your list of names are: ".title())
for nm in name:
    print(nm)

    
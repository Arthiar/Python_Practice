"""#[start:end:step], P->0, Y->1...N->5
text ="Hello"
print("Lets do slicing",text[0:2])
print("Lets do slicing",text[4:])
print("Lets do slicing",text[::2])
print("Lets do slicing",text[::-1])
for i in range(6):
    print(text.title())
    
for i in range(len(text)+1):
    print(text[:i])    
print("\n--------------")
for i in range(len(text)):
    print(text[i:])
    
print("\n------------------While loop----------------------------") 

i =1
# start from 0
while i <= len(text):
    print(text[:i])
    i += 1
else:
    print("Sorry. its just hello")
print("\n------------------------")


i = len(text)   # start from 6
while i > 0:
    print(text[:i])
    i -= 1

i = len(text)   # start from 6
while i >= 0:
    print(text[i:])
    i -= 1
    
    
    print("\n------------------Basics----------------------------") """
    
a=int(input("PLease enter a number for A: "))
b=int(input("PLease enter a number for B: "))

c=int(a+b)
if  c%2==0:
    print("the value is even")
else:
    print("The value is odd")
if a>b:
    print("A is greater than B")    
else:
    print("B is the greatest")   
    
    i=1
for i in range(1,6):
    print(a*i)
    i+=1

D= "Hello" #input("Enter a string: ")
print("Reversed string is:", D[::-1])

print("------------------------------------------------------------------------------------")

# Count letters in a word
word ="Hello" #input("Enter a word: ")
d = len(word) # len() gives length of string
print("The word has", d, "letters.")

print("------------------------------------------------------------------------------------")

# Find maximum in a list
numbers = [12, 45, 7, 99, 23, 5]
print("The list is:", numbers)
print("The maximum number is:", max(numbers))
print("The sum is:", sum(numbers))
print("------------------------------------------------------------------------------------")

number=int(input("Enter a number: "))
fact = 1
for i in range(1, number+1):
    fact *=i
print(f"The factorial of{number} is {fact}")
    
# Factorial of a number

num = int(input("Enter a number: "))

fact = 1
for i in range(1, num + 1):
    fact *= i   # multiply each number
print(f"Factorial of", num, "is", fact)

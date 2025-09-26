def place():
    location= 'Erode'
    new= location.replace('Erode','Gobi')
    print(new)
    place()

#list practice 
def list():
    numbers = [12, 45, 67, 23, 89, 34, 22, 90, 11, 56]
    fruits = ["apple", "banana", "mango", "orange", "grape", "kiwi", "pear", "pineapple"]
    names = ["Arthi", "Monica", "Daranya", "Aftab", "Raj", "Kumar", "Divya", "Anu"]
    songs = ["Shape of You", "Perfect", "Believer", "Despacito", "Senorita", "Hips Don't Lie"]
    mixed = [25, "hello", 3.14, True, "Python", 99, False]
    r=[]
    numbers.append(100)
    fruits.insert(2,"23")
    songs.pop()
    names = [n for n in names if n not in ["Monica", "Aftab"]]
    for i in mixed:
        r.insert(0,i)
    print("The latest list of numbers", numbers)
    print("The latest list of fruits", fruits)
    print("The latest list of names", names)
    print("The latest list if songs:", songs)
    print("THe reversed value is", r)
list()

#lets get input from list

def hello():
    a = list(map(int, input("Enter the values for a (comma separated): ").split(",")))
    n = list(map(int, input("Enter the values for n (comma separated): ").split(",")))

    if len(a) != len(n):
        print("Enter the numbers for both a and n equal")
        return

    result = []
    for i, j in zip(a, n):
        result.append(i + j)

    print("The sum of the values are:", result)

hello()


    
   
        
    


n = int(input("Enter a number: ")) 

def countdown(n):     
    if n == 0:
        print("💣 Boom!")
    else:
        print(n)
        countdown(n - 1)
        
countdown(n)   # pass n here

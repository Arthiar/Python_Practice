#Getting input from user for splitting the names/words
"""Sentence= input("Enter a sentence: ")
words= Sentence.split()
print(words)
unique=set(words)
print("The unique words of the sentence are: ", unique)
result=" ".join(unique)
print("The final senstence is ", result)"""

#Union, Intersection and Difference
A= set(map(int, input("Enter the number for A: ").split()))
B= set(map(int, input("Enter the number for B: ").split()))
print("The value of A are: ", A)
print("The value of A are: ", B)
C=(A.union(B))
D=(A.intersection(B))
E=(A.difference(B))
F=(B.difference(A))
print("The union is C:", C)
print("The intersection is D:", D)
print("The Diff btw AnB E:", E)
print("The Diff btw BnA F:", F)


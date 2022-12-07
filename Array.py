# Problema 4: Arreglos 
import random
A=[10]

for i in range (1,11,1):
    elemento=random.randrange(100)
    A.append(elemento)
    
print("Los elementos del arreglo son: ")
for i in range (1,11,1):
    print (f"A [",(i),"]->",A[i])  

print("\n")

print("En orden inverso: ")
for i in range (10,0,-1):
    print (f"A [",(i),"]->",A[i],end="  ")  
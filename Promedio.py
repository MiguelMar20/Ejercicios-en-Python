# Problema 2: Promedio 
n=int(input("Ingrese la cantidad de datos"))
print(n)
acum=0
for i in range(1,n+1) :
    dato=float(input("Ingrese el dato:"))
    acum=acum+dato

prom=acum/n
print(f"El promedio es {prom}")
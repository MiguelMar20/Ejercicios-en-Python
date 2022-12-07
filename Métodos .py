# Problema 3: Métodos 
def Saludar():
    print("Hola mundo!")

def CalcularDoble(num):
    res=num*2
    return res

def Triplicar(num):
    num*=3
    return num
    

print("Llamada a la funcion Saludar")
Saludar()

x=int(input("Ingrese un numero para x: "))
print(x)

print("Llamada a la funcion CalcularDoble (pasaje por valor)")
print("El doble de ",x," es ",CalcularDoble(x))
print("El valor original de x es ", x)

print("Llamada a la funcion Triplicar (pasaje por referencia)")
num=Triplicar(x)
print("El nuevo valor de x es ", num)

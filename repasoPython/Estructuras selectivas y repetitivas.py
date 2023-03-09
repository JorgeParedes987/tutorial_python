#Estructuras  repetitivas
"""
Una estructura repetitiva permite ejecutar una o varias instrucciones varias veces.
"""
#Estructura repetitiva While
"""
el bucle while o bucle mientras es un ciclo repetitivo basado en los resultados de una expresión lógica; 
"""
# Se ingresan un conjunto de n alturas de personas por teclado. El valor de la altura puede ser en metros o
# en centímetros(a elección de cada uno, lo comento para practicar con float). Mostrar el promedio de todas las alturas.
print("/////////////////////////////////////ESTRUCTURA REPETITIVA/////////////////////////////////")
print("EJEMPLO WHILE")
print("Programa que permite pedir al usuario un numero de personas y de acuerdo a ello se le pide la altura de cada uno para hacer un promedio")

personas=int(input("Cuantas personas hay:"))
x=1
suma=0
while x<=personas:
    altura=float(input("Ingrese la altura: "))
    suma=suma+altura
    x=x+1
promedio=suma/personas
print("El promedio es ")
print(promedio)#Estructura repetitiva for
"""
La instrucción for permite repetir una instrucción o una instrucción compuesta un número especificado de veces.
"""

#Realizar un programa que permita la carga de 5 valores por teclado y posteriormente, nos muestre la suma de los valores ingresados y su promedio.
print("Ejemplo con for")
print(" programa que permite la carga de 5 valores por teclado y posteriormente, nos muestre la suma de los valores ingresados y su promedio.")
suma=0
for x in range(5):
    num=int(input("Ingrese un valor:"))
    suma=suma+num
promedio=suma/5
print("La suma es: ")
print(suma)
print("El promedio es: ")
print(promedio)

print("///////////////////////ESTRUCUTURAS SELECTIVAS/////////////////////////////////")
#IF
"""
 la sentencia IF para determinar el flujo del programa en función de la evaluación de expresión. 
 """
print("Ejemplo con if")
print("Probar si b es mayor que  a")
a = int(input("Ingrese el valor de a"))
b = int(input("Ingrese el valor de b "))
if b > a:
    print(" b es mayor que a")
#Else
"""
 La setencia else se usa cuando hay dos condiciones por cumplir  
 """
print("Ejemplo con else si a es mayor o menor que b")
a = int(input("Ingrese el valor de a"))
b = int(input("Ingrese el valor de b "))

if a < b:
    print(" b es mayor que a")
else:
    print("a es mayor que b")
#Elif
"""
 La setencia Elif se usa cuando hay varias condiciones por cumplir  
 """
print("Ejemplo se ingresa dos numeros y con el elif se mira si a es mayor,menor o igual que b")
a = int(input("Ingrese el valor de a"))
b = int(input("Ingrese el valor de b "))

if a < b:
    print(" b es mayor que a")
elif a > b:
    print("a es mayor que b")
else:
    print("son iguales")
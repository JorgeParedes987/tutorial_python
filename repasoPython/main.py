# Tipos de datos primitivos
# Numeros enteros

numero1: int = 57
print(numero1)

numero2 = 24
print(numero2)

# numeros reales
numero3: float = 4.9
print(numero3)

numero4 = 5.0
print(numero4)

# booleanos
esColombiano: bool = True
esArgentino = False
print(esColombiano)

# Caracter y cadena de caracteres
mensaje = "cadena con una comilla simple ' , una comilla doble \" y uba  diagonal invertida\\"
print(mensaje)

# operadores
# Arimeticos
numero5 =  9
numero6 = 12
suma= numero5+numero6
multiplicacion= numero5*numero6
resto= numero5-numero6
division= numero5/numero6
modulo= numero5%numero6
print("La suma es " , suma)
print("La multiplicacion es " , multiplicacion)
print("La resto es " , resto)
print("La division es " , division)
print("La modulo es " , modulo)

#asignacion
x= 7
y=8
z=2
print(x)

# logicos
q= 5
print(q > 4 and q<9)

#or (o)
p=4
print(p>5 or p<10)

# not
print(not(p>2 and  q<7))
# Relacionales
valor1 = 7
valor2 = 9
print(valor1==valor2) #igualdad
print(valor1>valor2)  # mayor que
print(valor1<valor2) #menor que
print(valor1>= valor2) # Mayor igual que
print(valor1<= valor2) # Menor igual que
print(valor1!= valor2) #No igual

# Funciones
"""
    Las funciones son un bloque de codigo que solo se ejecutan cuando se llaman
"""
def mi_funcion():
    print("¡Feliz dia !")
mi_funcion() # Invocar la funcion

def mensaje(nombre , apellido):
    print("¡Feliz dia ! " +nombre + apellido)
mensaje("Triple" , "J")
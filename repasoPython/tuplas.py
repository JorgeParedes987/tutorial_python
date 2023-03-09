print("Tupla anidada")
tupla_anidada = ((1, 2, 3), ('a', 'b', 'c'), (True, False))
print("Indexación de tuplas:")
tupla = ('a', 'b', 'c', 'd', 'e')
print(tupla[0])
print(tupla[2:4])
print(tupla[-1])
print("Concatenación de tuplas:")
tupla1 = ('a', 'b', 'c')
tupla2 = ('d', 'e', 'f')
tupla_concatenada = tupla1 + tupla2
print(tupla_concatenada)
print("Desempaquetado de tuplas:")
tupla = ('Juan', 'Pérez', 25)
nombre, apellido, edad = tupla
print(nombre)
print(apellido)
print(edad)
print("Creación de tuplas a partir de listas:")
lista = [1, 2, 3, 4, 5]
tupla = tuple(lista)
print(tupla)
print("Uso de funciones integradas de tuplas:")
tupla = (1, 2, 3, 4, 5)
print(len(tupla))  # 5
print(max(tupla))  # 5
print(min(tupla))  # 1
print(sum(tupla))  # 15


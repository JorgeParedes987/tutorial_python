# Los diccionarios son poderosas estructuras de datos en Python que almacenan datos como pares de claves
print("Creación de un diccionario:")
diccionario = {'nombre': 'Juan', 'apellido': 'Pérez', 'edad': 25}
print("Acceso a los valores del diccionario:")
print(diccionario['nombre'])  # Juan
print(diccionario['edad'])  # 25
print("Actualización del valor de una clave:")
diccionario['edad'] = 30
print(diccionario)
print("Agregar un nuevo par de clave-valor al diccionario:")
diccionario['telefono'] = '123456789'
print(diccionario)
print("Eliminación de un par de clave-valor del diccionario:")
del diccionario['apellido']
print(diccionario)
print("Iteración a través de las claves y valores del diccionario:")
for clave, valor in diccionario.items():
    print(clave, valor)
print("Creación de un diccionario vacío y agregación de pares de clave-valor:")
diccionario_vacio = {}
diccionario_vacio['nombre'] = 'María'
diccionario_vacio['apellido'] = 'Gómez'
diccionario_vacio['edad'] = 35
print(diccionario_vacio)

print("Comprobación de si una clave está en el diccionario:")
if 'nombre' in diccionario_vacio:
    print('La clave "nombre" está en el diccionario')
print("Uso de la función len() para obtener la cantidad de pares de clave-valor en el diccionario:")
print(len(diccionario_vacio))  # 3

print("Creación de una lista:")
mi_lista = ["manzana", "pera", "banana", "naranja"]
print("Acceder a un elemento de la lista:")
print(mi_lista[0])
print("Añadir un elemento a la lista:")
mi_lista.append("uva")
print(mi_lista)
print("Eliminar un elemento de la lista:")
mi_lista.remove("pera")
print(mi_lista)
print("//////////////////////////////////////////LISTAS ENLAZADAS/////////////////////////////////")
print("Creación de una lista enlazada:")
class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None

nodo1 = Nodo(3)
nodo2 = Nodo(7)
nodo3 = Nodo(11)

nodo1.siguiente = nodo2
nodo2.siguiente = nodo3

print("Acceder a un elemento de la lista enlazada:")
print(nodo1.siguiente.valor)
print("Añadir un elemento a la lista enlazada:")
nodo4 = Nodo(15)
nodo3.siguiente = nodo4
print("Eliminar un elemento de la lista enlazada:")
nodo2.siguiente = nodo3.siguiente
nodo3.siguiente = None

print("/////////////////////////////////////Operaciones con listas:////////////////////////////////////////////")

print("Concatenar dos listas:")
lista1 = [1, 2, 3]
lista2 = [4, 5, 6]
lista_concatenada = lista1 + lista2
print(lista_concatenada)

print("Ordenar una lista:")
mi_lista = [5, 2, 9, 1, 7]
mi_lista.sort()
print(mi_lista)

print("Encontrar el valor máximo y mínimo de una lista:")
mi_lista = [5, 2, 9, 1, 7]
maximo = max(mi_lista)
minimo = min(mi_lista)
print(maximo)
print(minimo)

print("Obtener la longitud de una lista:")
mi_lista = [5, 2, 9, 1, 7]
longitud = len(mi_lista)
print(longitud)




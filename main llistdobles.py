from itemCrud import Item
from productCrud import Product
from SupplierCrud import Proveedor
from GymCrud import Gym
from CampusCrud import Campus
from userCrud import user

class Nodo(Item):
    def __init__(self, dato=None, siguiente=None, anterior=None):
        self.dato = dato
        self.siguiente = siguiente
        self.anterior = anterior

class ListaDoblementeEnlazada(Item):
    def __init__(self):
        self.cabeza = None
        self.cola = None
        self.contador = 0
    
    def insertar(self, dato):
        nodo = Nodo(dato)

        if self.cabeza is None:
            self.cabeza = nodo
            self.cola = self.cabeza
        else:
            nodo.anterior = self.cola
            self.cola.siguiente = nodo
            self.cola = nodo
        
        self.contador += 1
    
    def iterar(self):#Metodo de instancia
        actual = self.cabeza

        while actual:
            dato = actual.dato
            actual = actual.siguiente
            yield dato

    def insertar_inicio(self, dato):
        if self.cabeza is not None:
            nodo = Nodo(dato)
            nodo.siguiente = self.cabeza
            self.cabeza.anterior = nodo
            self.cabeza = nodo

            self.contador += 1
    
    def buscar(self, dato):
        for d in self.iterar():
            if dato == d:
                return True
        
        return False
    
    def eliminar(self, dato):
        actual = self.cabeza
        eliminado = False

        if actual is None:
            eliminado = False
        elif actual.dato == dato:
            self.cabeza = actual.siguiente
            self.cabeza.anterior = None
            eliminado = True
        elif self.cola.dato == dato:
            self.cola = self.cola.anterior
            self.cola.siguiente = None
            eliminado = True
        else:
            while actual:
                if actual.dato == dato:
                    # Antes: 2 = 3 = 5 = 7 = 11
                    # Actual: 3
                    # Después: 2 = 5 = 7 = 11
                    actual.anterior.siguiente = actual.siguiente
                    actual.siguiente.anterior = actual.anterior
                    eliminado = True
                actual = actual.siguiente
        
        if eliminado:
            self.contador -= 1
    
    def __getitem__(self, indice):
        if indice >= 0 and indice < self.contador:
            actual = self.cabeza

            for _ in range(indice - 1):
                actual = actual.siguiente
            
            return actual.dato
        else:
            raise Exception('Índice no válido. Está por fuera del rango.')
    
    def __setitem__(self, indice, dato):
        if indice >= 0 and indice < self.contador:
            actual = self.cabeza

            for _ in range(indice - 1):
                actual = actual.siguiente
            
            actual.dato = dato
        else:
            raise Exception('Índice no válido. Está por fuera del rango.')


listaItem = ListaDoblementeEnlazada()
print('Cantidad después de crear la lista:', listaItem.contador)
listaItem.insertar(2)
print('Cantidad después de insertar un elemento en la lista:', listaItem.contador)

item1=Item('1','Colchoneta',8,'activo','Ejercicios ABS','Stool','Jisus')
item2=Item('2','balones',1,'activo','Ejercicios ','Stool','adidas')
item3=Item('3','Cuerdas',30,'activo','Ejercicios ','Stool','adidas')
item4=Item('4','Sillas',15,'activo','Ejercicios ','Stool','adidas')
item5=Item('5','Guantes',45,'activo','Ejercicios ','Stool','adidas')
print()
listaItem.insertar(item1)
listaItem.insertar(item2)
listaItem.insertar(item3)
listaItem.insertar(item4)
listaItem.insertar(item5)

print('Cantidad actual de elementos:', listaItem.contador)

print()

for d in listaItem.iterar():
    print(d)

print()

listaItem.insertar_inicio(0)
listaItem.insertar_inicio(1)
print('Cantidad de elementos después de insertar el valor cero:', listaItem.contador)

for d in listaItem.iterar():
    print(d)

print()

print('Búsqueda de un dato')
numero = 19
print('¿Se halla 19 en la lista?:', listaItem.buscar(numero))
numero = 7
print('¿Se halla 7 en la lista?:', listaItem.buscar(numero))

print()

print('Eliminación de datos:')
numero = 1
print('Cantidad de elementos antes de la eliminación:', listaItem.contador)
listaItem.eliminar(numero)
print('Cantidad de elementos después de la eliminación:', listaItem.contador)
print('¿Este el valor 1 en la lista?:', listaItem.buscar(numero))

print()

print('Acceso a un elemento por medio de su índice:')
# indice = -1
# print('Valor en la posición %i es igual a %i' % (indice, listaItem[indice])) # Genera excepción
indice = 0
print('Valor en la posición %i es igual a %i' % (indice, listaItem[indice]))
indice = 2
print('Valor en la posición %i es igual a %i' % (indice, listaItem[indice]))
indice = 3
print('Valor en la posición %i es igual a %i' % (indice, listaItem[indice]))
indice = 4
print('Valor en la posición %i es igual a %i' % (indice, listaItem[indice]))
# indice = 7
# print('Valor en la posición %i es igual a %i' % (indice, listaItem[indice])) # Genera excepción

print()

print('Modificación valores de la lista a partir de un índice:')

# #listaItem[-1] = 19 # Genera excepción
print('Cantidad actual de elementos: %i' % listaItem.contador)
print('Contenido en la posición 5 antes de la modificación: %i' % listaItem[5])
listaItem[5] = 17
print('Contenido en la posición 5 después de la modificación: %i' % listaItem[5])
from typing import Any
from item import Item
from product import Product
from Supplier import Proveedor
from Gym import Gym
from Campus import Campus
from user import user

if __name__ == '__main__':
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
                        actual.anterior.siguiente = actual.siguiente
                        actual.siguiente.anterior = actual.anterior
                        eliminado = True
                    actual = actual.siguiente
            
            if eliminado:
                self.contador -= 1
        
        def __getitem__(self, indice):
            if indice >= 1 and indice < self.contador:
                actual = self.cabeza

                for _ in range(indice - 1):
                    actual = actual.siguiente
                
                return actual.dato
            else:
                raise Exception('Índice no válido. Está por fuera del rango.')
        
        def __setitem__(self, indice, dato):
            if indice >= 1 and indice < self.contador:
                actual = self.cabeza

                for _ in range(indice -1):
                    actual = actual.siguiente
                
                actual.dato = dato
            else:
                raise Exception('Índice no válido. Está por fuera del rango.')


    listaItem = ListaDoblementeEnlazada()
    print('Cantidad antes de insertar un elemento en la lista:', listaItem.contador)

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
    #listaItem.insertar(item5)

    print('Cantidad actual de elementos:', listaItem.contador)
    print()

    for d in listaItem.iterar():
        print(d)

    print()

    listaItem.insertar_inicio(item5)
    #listaItem.insert(dato=item5,pos=0)
    print('Cantidad de elementos después de insertar el elementos: ', listaItem.contador)

    for d in listaItem.iterar():
        print(d)

    print()


    print('Eliminación de datos:')
    item1 = item1
    listaItem.eliminar(item1)
    print('Cantidad de elementos después de eleminar el elemento: ', listaItem.contador)
    for d in listaItem.iterar():
        print(d)

    print()

    """print('Eliminación de datos especificando cualquier elemento:')
    item5 = item5
    print('Cantidad de elementos antes de la eliminación:', listaItem.contador)
    listaItem.eliminar(item5)

    print('Cantidad de elementos después de eleminar el elemento: ', listaItem.contador)
    for d in listaItem.iterar():
        print(d)"""

    print()

    print('Insertando valores de la lista a partir de un índice:')
    print('Cantidad actual de elementos: %i' % listaItem.contador)
    print('Contenido en la posición 3 antes de la modificación: ' ,listaItem[3])
    listaItem[3] = item3.getNombre
    print('Contenido en la posición 3 después de la modificación: ', listaItem[3])
        




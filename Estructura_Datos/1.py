class NodoLista():
    atrib1 = None
    atrib2 = None
    
def Genera_Nodo():
    nodo = NodoLista()
    nodo.atrib1 = int(input('Ingrese atrib1 = '))
    nodo.atrib2 = input('Ingrese atrib2 = ')
    return nodo

def Push_Lista():
    global Maximo
    if len(lista) == Maximo:
        print('No se puede insertar. Overflow')
    else:
        nodo = Genera_Nodo()
        if len(lista) == 0:
            lista.append(nodo)
        else:
            if nodo.atrib1 < lista[0].atrib1:
                lista.insert(0, nodo)
            else:
                i = 0
                while i < len(lista) and nodo.atrib1 >= lista[i].atrib1:
                    i += 1
                lista.insert(i, nodo)
def Pop_Lista():
    if len(lista) == 0:
        print('Underflow. No quedan elementos en la lista')
        return None
    else:
        valor_a_eliminar = int(input('Ingrese atrib1 de nodo a eliminar = '))
        i = 0
        while i < len(lista) and valor_a_eliminar != lista[i].atrib1:
            i += 1
        if i == len(lista):
            print('El valor requerido no esta en la lista')
            return None
        else:
            print('El valor requerido está en la posicion ',i)
            nodo = lista[i]
            lista.pop(i)
            return nodo

def Listar():
    for i in range(len(lista)):
        print(lista[i].atrib1, lista[i].atrib2)
                
#############

lista = []
Maximo = int(input('Ingrese número máximo de elementos en la lista: '))

Opcion = 0

while Opcion != 4:
    print(""" Opciones a ingresar
          1. Insertar (Push)
          2. Eliminar (Pop)
          3. Listar
          4. Salir
          """)
    Opcion = int(input('Ingrese una Opcion: '))
    if Opcion == 1: Push_Lista()
    elif Opcion == 2: 
        nodo_eliminado = Pop_Lista()
        if nodo_eliminado != None: print('El valor eliminado es ', nodo_eliminado.atrib1)
    elif Opcion == 3: Listar()
    elif Opcion == 4: input('Fin del programa')
    else: print('Error, fuera de rango')

input()
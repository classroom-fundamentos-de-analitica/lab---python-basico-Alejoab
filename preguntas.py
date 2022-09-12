"""
Laboratorio de Programación Básica en Python para Manejo de Datos
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

No puede utilizar pandas, numpy o scipy. Se debe utilizar solo las funciones de python
básicas.

Utilice el archivo `data.csv` para resolver las preguntas.


"""
import re

archivo = open("data.csv").readlines()


def pregunta_01():
    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """
    registros = [i.split("\t") for i in archivo]

    suma = sum(int(x[1]) for x in registros)

    return suma


def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como la lista
    de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [
        ("A", 8),
        ("B", 7),
        ("C", 5),
        ("D", 6),
        ("E", 14),
    ]

    """

    registros = [i.split("\t") for i in archivo]
    dicti = {}

    for i in registros:
        if i[0] in dicti:
            dicti[i[0]] += 1
        else:
            dicti[i[0]] = 1

    lista = list(dicti.items())
    lista = sorted(lista, key = lambda x: x[0])

    return lista


def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como una lista
    de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [
        ("A", 53),
        ("B", 36),
        ("C", 27),
        ("D", 31),
        ("E", 67),
    ]

    """

    registros = [i.split("\t") for i in archivo]
    dicti = {}

    for i in registros:
        if i[0] in dicti:
            dicti[i[0]] += int(i[1])
        else:
            dicti[i[0]] = int(i[1])
        

    lista = list(dicti.items())
    lista = sorted(lista, key = lambda x: x[0])

    return lista



def pregunta_04():
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la cantidad de
    registros por cada mes, tal como se muestra a continuación.

    Rta/
    [
        ("01", 3),
        ("02", 4),
        ("03", 2),
        ("04", 4),
        ("05", 3),
        ("06", 3),
        ("07", 5),
        ("08", 6),
        ("09", 3),
        ("10", 2),
        ("11", 2),
        ("12", 3),
    ]

    """
    registros = [i.split("\t") for i in archivo]
    dicti = {}

    for i in registros:
        mes = re.findall("-([0-9]{2})-", i[2])[0]
        print(mes)
        if mes in dicti:
            dicti[mes] += 1
        else:
            dicti[mes] = 1
        

    lista = list(dicti.items())
    lista = sorted(lista, key = lambda x: x[0])

    return lista

def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2 por cada
    letra de la columa 1.

    Rta/
    [
        ("A", 9, 2),
        ("B", 9, 1),
        ("C", 9, 0),
        ("D", 8, 3),
        ("E", 9, 1),
    ]

    """
    registros = [i.split("\t") for i in archivo]
    letras = sorted(set([i[0] for i in registros]))

    lista = []
    for letra in letras:
        maximo = max(list(filter(lambda x: x[0] == letra, registros)), key = lambda x: x[1])[1]
        minimo = min(list(filter(lambda x: x[0] == letra, registros)), key = lambda x: x[1])[1]
    
        lista.append((letra, int(maximo), int(minimo)))

    return lista

def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras corresponde a
    una clave y el valor despues del caracter `:` corresponde al valor asociado a la
    clave. Por cada clave, obtenga el valor asociado mas pequeño y el valor asociado mas
    grande computados sobre todo el archivo.

    Rta/
    [
        ("aaa", 1, 9),
        ("bbb", 1, 9),
        ("ccc", 1, 10),
        ("ddd", 0, 9),
        ("eee", 1, 7),
        ("fff", 0, 9),
        ("ggg", 3, 10),
        ("hhh", 0, 9),
        ("iii", 0, 9),
        ("jjj", 5, 17),
    ]

    """

    registros = [i.split("\t") for i in archivo]
    dicti = {}

    for i in registros:
        
        for j in i[4].split(","):
            codigo, numero = re.findall("(.*):(.*)", j)[0]
            if codigo in dicti:
                dicti[codigo].append(int(numero))
            else:
                dicti[codigo] = [int(numero)]
    
    lista = []
    for letra in dicti.keys():
        maximo = max(dicti[letra])
        minimo = min(dicti[letra])
        lista.append((letra, minimo, maximo))

    lista = sorted(lista, key = lambda x: x[0])

    return lista


def pregunta_07():
    """
    Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla contiene un
    valor posible de la columna 2 y una lista con todas las letras asociadas (columna 1)
    a dicho valor de la columna 2.

    Rta/
    [
        (0, ["C"]),
        (1, ["E", "B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E", "E", "D"]),
        (4, ["E", "B"]),
        (5, ["B", "C", "D", "D", "E", "E", "E"]),
        (6, ["C", "E", "A", "B"]),
        (7, ["A", "C", "E", "D"]),
        (8, ["E", "D", "E", "A", "B"]),
        (9, ["A", "B", "E", "A", "A", "C"]),
    ]

    """

    registros = [i.split("\t") for i in archivo]
    dicti = {}

    for i in registros:
        if int(i[1]) in dicti:
            dicti[int(i[1])].append(i[0])
        else:
            dicti[int(i[1])] = [i[0]]

    lista = list(dicti.items())
    lista = sorted(lista, key = lambda x: x[0])


    return lista


def pregunta_08():
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla contiene  el valor
    de la segunda columna; la segunda parte de la tupla es una lista con las letras
    (ordenadas y sin repetir letra) de la primera  columna que aparecen asociadas a dicho
    valor de la segunda columna.

    Rta/
    [
        (0, ["C"]),
        (1, ["B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E"]),
        (4, ["B", "E"]),
        (5, ["B", "C", "D", "E"]),
        (6, ["A", "B", "C", "E"]),
        (7, ["A", "C", "D", "E"]),
        (8, ["A", "B", "D", "E"]),
        (9, ["A", "B", "C", "E"]),
    ]

    """

    registros = [i.split("\t") for i in archivo]
    dicti = {}

    for i in registros:
        if int(i[1]) in dicti:
            dicti[int(i[1])].append(i[0])
        else:
            dicti[int(i[1])] = [i[0]]

    lista = list(dicti.items())
    lista = sorted(lista, key = lambda x: x[0])

    lista = list(map(lambda x: (x[0], sorted(list(set(x[1])))), lista))

    return lista



def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que aparece cada
    clave de la columna 5.

    Rta/
    {
        "aaa": 13,
        "bbb": 16,
        "ccc": 23,
        "ddd": 23,
        "eee": 15,
        "fff": 20,
        "ggg": 13,
        "hhh": 16,
        "iii": 18,
        "jjj": 18,
    }

    """

    registros = [i.split("\t") for i in archivo]
    dicti = {}

    for i in registros:
        
        for j in i[4].split(","):
            codigo, _ = re.findall("(.*):(.*)", j)[0]
            if codigo in dicti:
                dicti[codigo] += 1
            else:
                dicti[codigo] = 1
    

    return dicti



def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la columna 1 y la
    cantidad de elementos de las columnas 4 y 5.

    Rta/
    [
        ("E", 3, 5),
        ("A", 3, 4),
        ("B", 4, 4),
        ...
        ("C", 4, 3),
        ("E", 2, 3),
        ("E", 3, 3),
    ]


    """

    registros = [i.split("\t") for i in archivo]
    lista = []

    for i in registros:
        letra = i[0]
        segundo = len(i[3].split(","))
        tercero = len(i[4].split(","))
        lista.append((letra, segundo, tercero))

    return lista



def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada letra de la
    columna 4, ordenadas alfabeticamente.

    Rta/
    {
        "a": 122,
        "b": 49,
        "c": 91,
        "d": 73,
        "e": 86,
        "f": 134,
        "g": 35,
    }


    """
    
    registros = [i.split("\t") for i in archivo]
    dicti = {}

    for i in registros:
        
        for j in i[3].split(","):
            if j in dicti:
                dicti[j] += int(i[1])
            else:
                dicti[j] = int(i[1])
    

    return dicti



def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor la suma de
    los valores de la columna 5 sobre todo el archivo.

    Rta/
    {
        'A': 177,
        'B': 187,
        'C': 114,
        'D': 136,
        'E': 324
    }

    """
    registros = [i.split("\t") for i in archivo]
    letras = list(set([i[0] for i in registros]))
    dicti = {}

    for letra in letras:
        for i in list(filter(lambda x: x[0] == letra, registros)):        
            for j in i[4].split(","):
                _, numero = re.findall("(.*):(.*)", j)[0]
                if letra in dicti:
                    dicti[letra] += int(numero)
                else:
                    dicti[letra] = int(numero)


    return dicti
def analizarLista(lista1, lista2):
    #Parseamos las listas a conjuntos
    conjunto1 = set(lista1)
    conjunto2 = set(lista2)

    #Extraemos las intersecciones
    interseccion = list(conjunto1.intersection(conjunto2))

    #Extraemos las uniones
    union = list(conjunto1.union(conjunto2))

    #Diferencia Simetrica
    diferencia = list(conjunto1.symmetric_difference(conjunto2))

    diccionario = {"interseccion": interseccion, "union": union, "diferencia":diferencia}

    return diccionario

lista1 = [1,5,7,8,3,5,-2]
lista2 = [3,8,15,1,0,-2]

resultado = analizarLista(lista1, lista2)

print("El diccionario devuelto es: ", resultado)
def listaRecibida(listaNumeros):
  listaSinNegativos = []
  #Recorremos los numeros de la lista
  for num in listaNumeros:
    #Si es negativo no lo incluimos, si es positivo agregamos
    if num > 0:
      listaSinNegativos.append(num)

  #Quitamos duplicados con Set
  listaSinDuplicados = set(listaSinNegativos)
  #Ordenamos
  listaFinal = sorted(listaSinDuplicados)
  #Devolvemos la lista actualizada
  return listaFinal

lista = [1, 25, -5, 2, 3, -3 , 2, 3, 8, 12, 11]
resultado = listaRecibida(lista)
print("Lista original: ", lista)
print("Lista actualizada: ", resultado)



  
  

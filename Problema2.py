import string

def listaPalabras(listaPalabras, ruta):
    #Modificacmos la lista de palabras a minusculas y le damos el valor
    palabrasDic = {}
    for palabra in listaPalabras:
        palabrasDic[palabra.lower()] = 0
    #Activamos bloque try-catch por posibles errores con el texto.
    try:
        #Abrimos el txt en modo lectura
        with open(ruta, 'r', encoding='utf-8') as fichero:
            contenido = fichero.read()
        
        #Una vez tenemos el contenido del fichero lo pasamos a minusculas
        contenido = contenido.lower()

        #Quitamos los simbolos de puntuacion, y los cambiamos por espacios
        for signo in string.punctuation:
            contenido = contenido.replace(signo, " ")
        
        #Separamos el texto en lista de palabras
        palabrasTexto = contenido.split()

        #Comprobamos las palabras del texto sobre las claves del diccionario y vamos contenando cada vez que estén
        for p in palabrasTexto:
            if p in palabrasDic:
                palabrasDic[p] += 1

        #Ordenamos el diccionario por cada palabra
        palabrasDicOrdenada = dict(sorted(palabrasDic.items()))

        return palabrasDicOrdenada

    except FileNotFoundError:
        print("Error, no se encontró la ruta")
        return {}
    

rutaArchivo = "textoProblema2.txt"
listaBuscada = ["lista", "PALABRAS", "valor", "palabra"]

resultado = listaPalabras(listaBuscada, rutaArchivo)

print("El resultado es: ", resultado)
        

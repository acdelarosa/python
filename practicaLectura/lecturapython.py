#Para que me devuelva todo el contenido

""" with open ("practicaLectura\lectura.txt", "r") as archivo:
    contenido=archivo.read()
    print(contenido) """


#Para que lea línea por línea:


""" with open ("practicaLectura\lectura.txt", "r") as archivo:
    lineas=archivo.readlines()
    print(lineas) """

#Con esto cuando se imprime contenido el cursor como imprimio todo el contenido, el cursor se queda en lo del final y por eso cuando
#se pide que imprima líneas devuelve un objeto vacío. Para evitar que devuelva un objeto vacío se debe usar el método SEEK(), de esta forma
#seek(0) ahí estamos haciendo que el cursor vuelva al puesto cero

with open ("practicaLectura\lectura.txt", "r") as archivo:
    contenido=archivo.read()
    archivo.seek(0)
    lineas=archivo.readlines()
    print(lineas)
    print(contenido)

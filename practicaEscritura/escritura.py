#Vamos a leer y escribir un archivo con r+
#con w se sobreescribe
#con r solo se lee
#con a se agrega al final

#\n esto es un salto de línea

with open ("practicaEscritura\lectura.txt", "a+") as archivo:
    archivo.write("Probando 1\n")
    archivo.write("Probando 2\n")
    archivo.write("Probando 3\n")
    archivo.close()

with open ("practicaEscritura\lectura.txt", "r") as archivo:
    contenido=archivo.read()
    print(contenido)
    archivo.close
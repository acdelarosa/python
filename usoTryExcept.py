def leerArchivo():
    try:
        with open ("practicaLectura\lectura.txt", "r") as archivo:
            contenido=archivo.read()
            print(contenido)
    except FileNotFoundError:
        #Este bloque se ejecuta si el archivo no se encuentra
        print("Error. El archivo de 'lectura.txt' no existe")
    except PermissionError:
        #Este bloque se ejecuta si se denegaron los permisos para leer el archivo
        print("Error. Permiso denegado para acceder al archivo 'lectura.txt")
    except Exception as e:
        #este bloque de código atrapa cualquier otro error
        print(f"Se produjo un error inesperado {e}")
    else:
        #este bloque de código se ejecuta si no hubo errores
        print("El archivo fue leído exitosamente")
    finally:
        #Este bloque de código se ejecuta hayan habido o no errores o excepciones
        print("Operación de lectura finalizada")

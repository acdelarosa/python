nombre=input("Por favor ingrese su nombre: ")
edad=input("Por favor ingrese su edad: ")
direccion=input("Por favor ingrese su direccion: ")

#para escribir en el archivo
with open ("ejercicioNombre\datos.txt", "a+") as archivo:
    archivo.write(f"Nombre: " + '\n' + nombre + '\n')
    archivo.write(f"Edad: " + '\n' + edad + '\n')
    archivo.write(f"Dirección: " + '\n' + direccion + '\n')
    archivo.close()

#para mostrar los datos guardados
with open ("ejercicioNombre\datos.txt", "r") as archivo:
    contenido=archivo.read()
    print(contenido)
    archivo.close
    
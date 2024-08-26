### 1. `append()`   
""" Ejercicio:** Tienes una lista de nombres de empleados y necesitas añadir nuevos empleados a la lista. 
Añade los nombres "Ana" y "Pedro" a la lista.
 """
###print(empleados)  # Salida esperada: ["Juan", "María", "Luis", "Ana", "Pedro"]

###RESOLUCION

""" empleados =  ["Juan", "María", "Luis"]
empleados.extend(["Ana", "Pedro"])
print(empleados) """

 ###Ejercicio:
""" Tienes dos listas de proyectos realizados por diferentes equipos. 
Necesitas combinar estas listas en una sola lista de todos los proyectos realizados.
print(proyectos_equipo1) 
 # Salida esperada: ["Proyecto A", "Proyecto B", "Proyecto C", "Proyecto D"] """

###RESOLUCIÓN

""" Concatenar """

""" lista1= ["Proyecto A"]
lista2 =["Proyecto B"]
lista3= ["Proyecto C"]
lista4 =["Proyecto C"]

proyectos = [lista1 + lista2  + lista3 + lista4]
print(proyectos)
 """


###EJERCICIO 3

""" Tienes una lista de tareas pendientes y necesitas agregar una tarea urgente al principio de la lista.
print(tareas)  
# Salida esperada: ["Tarea Urgente", "Tarea 1", "Tarea 2", "Tarea 3"] """

###RESOLUCIÓN

""" lista = ["Tarea 1", "Tarea 2", "Tarea 3"]
lista.insert(2, "Tarea Urgente")
print(lista) """


###EJERCICIO
""" Tienes una lista de productos en el inventario y necesitas eliminar un producto que se ha vendido. Elimina el producto "Producto B" de la lista.

print(inventario)  # Salida esperada: ["Producto A", "Producto C", "Producto D"]
"""
""" inventario= ["Producto A", "Producto B","Producto C", "Producto D"]  """

###RESOLUCIÓN

##Método

""" inventario= ["Producto A", "Producto B","Producto C", "Producto D"]
inventario.remove("Producto B")
print(inventario) """

### EJERCICIO 5 (POP)
""" Tienes una lista de clientes esperando en la fila para ser atendidos. 
Atiende (elimina y retorna) al último cliente de la fila.

print(ultimo_cliente)  # Salida esperada: "Cliente 3"
print(clientes)  # Salida esperada: ["Cliente 1", "Cliente 2"]
 """


###RESOLUCIÓN

""" clientes=["Cliente 1", "Cliente 2", "Cliente 3"]
clientes_por_atender = clientes.pop()
print(f"Estos son los clientes que ya fueron atendidos {clientes}")
print(f"Estos son los clientes que faltan atender {clientes_por_atender}")
 """



### EJERCICIO 6 (INDEX)
""" **Ejercicio:** Tienes una lista de números de pedido y necesitas encontrar la posición del pedido número 1024 en la lista.

# Encontrar la posición del pedido número 1024
indice_pedido = pedidos.index(1024)
print(indice_pedido)  # Salida esperada: 2 """

###RESOLUCIÓN

""" pedidos=["pedido 1", "pedido 8282", "pedido 1024", "pedido 49", "pedido 50", "pedido 59", "pedido 70"]
indice_pedido= pedidos.index("pedido 1024")
print(indice_pedido) """





### EJERCICIO 7 (SORT)

""" Tienes una lista de puntuaciones de exámenes y necesitas ordenarlas en orden ascendente.

print(puntuaciones)  # Salida esperada: [75, 85, 88, 91, 92] """

###RESOLUCIÓN
""" puntuaciones = [75, 85, 31, 29, 28, 91, 92, 0.3, 0.44, -2]
puntuaciones.sort()
print(puntuaciones) """





### EJERCICIO 8 (REVERSE)
""" Tienes una lista de eventos en orden cronológico y necesitas invertir el orden para mostrarlos en orden inverso.

print(eventos)  # Salida esperada: ["Evento 3", "Evento 2", "Evento 1"] """

###RESOLUCIÓN

""" eventos = ["Evento 1", "Evento 2", "Evento 3"]
eventos.reverse()
print(eventos) """






### EJERCICIO 9 (COUNT)
""" Tienes una lista de respuestas a una encuesta y necesitas contar cuántas veces aparece la respuesta "Sí".
print(conteo_si)  # Salida esperada: 4 """

###RESOLUCIÓN

""" Encuesta= ["Sí", "No", "Sí", "Sí", "Sí", "Sí", "Sí", "No"]
conteo_si = Encuesta.count("Sí")
print(conteo_si) """







###EJERCICIO 10 (CLEAR)
""" Tienes una lista de datos temporales que ya no son necesarios y necesitas vaciar la lista.
print(datos_temporales)  # Salida esperada: [] """

###RESOLUCIÓN
""" datos_temporales = ["gato", "perro", "rana", "saltamontes", "salamandra"]
print(datos_temporales)
datos_temporales.clear()
print(datos_temporales) """
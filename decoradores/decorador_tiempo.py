import time

def medir_tiempo(func):
    def funcion_decorada():
        inicio=time.time()
        resultado=func()
        fin=time.time()
        print(f"Tiempo de ejecución de {func.__name__}: {fin - inicio} segundos")
        return resultado
        return funcion_decorada
    

#time.sleep() sirve para esperar el tiempo que quieres, se mide en segundos

""" @medir_tiempo
def ejemplo_funcion(num):
    iniciando=2+2
    print("Iniciando")
    time.sleep(2)
    print("Función completada")


ejemplo_funcion() """


##Así se importa
###  from ..decoradores.decorador_tiempo import medir_tiempo





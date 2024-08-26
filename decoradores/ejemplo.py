def miDecorador(func):
    def wrapper():
        print("Inicio de datos de individuo")
        func
        print("Fin de datos de individuo")
        return wrapper
def aplicar_descuento(descuento):
    def decorador(funcion):
        def wrapper(precio):
            return funcion(precio*(1-descuento))

@aplicar_descuento
def precio_final(precio):
    print(f"El precio final después del descuento es: ${precio:.2f}")


precio_final(100)
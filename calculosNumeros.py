import math
""" import numpy """

""" para ver si es par """
a=-18

print(a%2==0)

""" para ver si es impar """

print(a%2==1)

""" uso de and y or """

print(a%2==0 and a>=1)
print(a%2==0 or a>=1)

""" para que solo saque una letra del string """

b="Hello World"
print(b[4])

""" para sacar varias letras del numero tal al otro """

print(b[4:9])

""" para obtener todo lo que viene después del número seleccionado """
print(b[4:])

""" para obtener todo lo anterior al número seleccionado """

print(b[:9])

""" para obtener el largo de la variable """

print(len(b))

""" para partir según algo determinado """

print(b.split("i"))

print(numpy.__version__)
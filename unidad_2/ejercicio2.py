"""
El programa debe:
- pedir en orden el Nombre, apellido, edad y numero de calzado
- verificar que cada uno sea el tipo de variable correcto (IMPORTANTE)
- en caso verdadero imprimir de la siguiente manera el resultado:

  ejemplo

  Nombre: Lionel

  Apellido: Messi

  Edad: 34

  Numero de Calzado: 42.5

- en caso contrario imprimir error
"""
try:
    nombre=input("ingrese su nombre:")
    apellido=input("ingrese su apellido: ")
    edad=int(input("cual es tu edad:"))
    calzado=float (input("cual es tu calzado"))
    print(f("buenas noches ,el nombre es {nombre} y el  apellido es {apellido}.\n tiene {edad} años y calzoa del {calzado}"))
except:
    print("los datos NO corresponde:")    
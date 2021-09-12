"""
Agencia de autos:

El programa cuenta con tres marcas de autos y su precio.

El programa debe:

pedir al usuario que ingrese la cant de dinero que dispone.
verificar que la cantidad ingresada sea un numero y sino mostrar error
verificar la cantidad de ingresada e indicar que auto o autos puede comprar
Ford = 10000
Renault = 11000
Chevrolet = 15000
"""
Ford=10000
Renaut=11000
Chevrolet=15000
try:
    dinero_disponible=float(input("ingrese dinero que posee:")) 
    if dinero_disponible >=(Ford)
    print("usted puede comprar un Ford ")
    if dinero_disponible >=(Renaut)
    print ("usted puede comprar Renaut ")
    if dinero_disponible>=(Chevrolet)
    print("usted puede comprar un Chevrolet")
else:
    print("No le alcanza ")    
except:
    print("los datos deben ser numeros unicamente ")    
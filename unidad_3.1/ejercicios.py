"""
El programa debe :
*    Pedir al usuario un string
*    Determinar si una cadena esta en minusculas o mayusculas
"""
try:
    palabra=input("ingrese una palabra o cadena de caracters:")       
    if palabra.islower():
        print("tu cadena de caracteres esta en minuscula ")
    else:
        print("esta en mayuscula ")    
except:
    print("esta mal")        
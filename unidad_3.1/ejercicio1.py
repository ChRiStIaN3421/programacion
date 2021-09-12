"""
El programa debe :
*   Almacenar una variable `contraseña` con una contraseña
*   Preguntar al usuario por la contraseña e imprimir por pantalla si la contraseña introducida por el usuario coincide o no con la variable
 **IMPORTANTE**: sin tener en cuenta mayúsculas y minúsculas.(metodos string)
*   no debe generar errores
"""
try:
    contraseña="somosloscracks23"
    usuario=str(input("ingrese la clave"))
    if usuario==contraseña.lower():
        print("su contraseña es correcta")
    else:
        print("su contraseña es incorrecta")      
except:
    print("error")
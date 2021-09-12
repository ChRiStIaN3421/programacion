"""
El programa debe:
*   mostrar el eco de todo lo que el usuario introduzca hasta que el usuario escriba “salir” que terminará.
*  si el usuario escribe "hola" o "chau" que no se haga el ecohola
"""
while True:
    palabra=input("Introduzca una palabra: ")
    if palabra=="salir":
        print("Ha introducido la palabra clave para salir del programa!!")
        break
    elif palabra=="hola" or  palabra=="chau":
        continue
    else:
       print(f"Usted ingreso {palabra}")
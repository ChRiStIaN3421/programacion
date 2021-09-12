"""
El programa debe:
*   Pedir al usuario una palabra
*   Verificar que sea una palabra y no un numero
*   Mostrar por pantalla las letras una a una
*   No producir errores
"""
while True:
    try:
        palabra=input("ingrese una palabra : ")
        if palabra.isalpha():
            for i in (palabra):
             print(i)
            else:
              print(f"ingreso una palabra : su palabra es {palabra} ")       
        break 
    except:
         print("error de sintexis ")    

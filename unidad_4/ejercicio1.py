"""
El programa debe:
*   Contar con 4 funciones (suma, resta, división y multiplicación)
*   Contar con un menu donde debe pedir al usuario que operacion realizar
*   Pedir los dos numero para operar y devolver el resultado al usuario
*   Gestionar posibles errores
"""
def suma (a,b):
    suma=float(a)+float(b)
    return suma

def resta (a,b):
    resta=float(a)+float(b)   
    return resta 

def divisor (a,b):
    try:
        divisor=round(float(a)/float(b),2)   
        
    except:
        print("la division genero un error ")   
        divisor="error" 
    return divisor

def multiplicador (a,b):
    multiplicador=float(a)*float(b)   
    return multiplicador   

def pedir_numero():
    while True:
        try:
            num1=float(input("1* argumneto: "))    
            num2=float(input("2* argumento: "))
            break
        except:
            print("argumento incorrecto")

    return num1,num2        


while True:
        condicion=input(
"""por favor ingrese una opcion 
        1-suma
        2-resta
        3-divicion
        4-multiplicacion
        5-salir
Numero : """)  
        if (condicion=="1") :
            a,b=pedir_numero()
            print(f"la suma de {a} + {b}={suma(a,b)}")
        elif (condicion== "2"):
              a,b=pedir_numero()
              print(f"la resta de {a} - {b}={resta(a,b)}")
        elif (condicion== "3"):
            a,b=pedir_numero()
            print(f"la multiplicacion de {a} x {b}={multiplicador(a,b)}")
        elif (condicion== "4"):
            a,b=pedir_numero()
            print(f"la division de {a}/{b}={divisor(a,b)}")
        elif (condicion== "5"):
            break
        else:
            print("ninguna opcion es correcta") 
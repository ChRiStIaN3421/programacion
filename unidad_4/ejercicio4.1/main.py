import funciones as fn 
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
            a,b=fn.pedir_numero()
            print(f"la suma de {a} + {b}={fn.suma(a,b)}")
        elif (condicion== "2"):
              a,b=fn.pedir_numero()
              print(f"la resta de {a} - {b}={fn.resta(a,b)}")
        elif (condicion== "3"):
            a,b=fn.pedir_numero()
            print(f"la multiplicacion de {a} x {b}={fn.multiplicador(a,b)}")
        elif (condicion== "4"):
            a,b=fn.pedir_numero()
            print(f"la division de {a}/{b}={fn.divisor(a,b)}")
        elif (condicion== "5"):
            break
        else:
            print("ninguna opcion es correcta") 
dinero_disponible=50000
"""ingrese dinero al sistema  y actualiza el saldo"""
def ingresar_y_actualizar(dinero_disponible):
    while True:
        try:

         dinero_ingresar=float(input("ingrese dinero a depositar: "))
         break
        except:
            print("error en los parametros ")
        if dinero_ingresar > 0:
           break
        else:
            print("por favor ingrese una suma positiva ")    
    dinero_disponible+=dinero_ingresar        
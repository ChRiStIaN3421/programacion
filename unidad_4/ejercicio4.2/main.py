import funciones_saldo as fs
import funcion_autenticar as fa

dinero_disponible=50000
condicion=True
while condicion:
 condicion=fa.validar_usuario()

    while True:
            opcion=input(
        """por favor ingrese una opcion 
                1-Consultar saldo
                2-Ingresar dinero
                3-Retirar dinero
                4-salir
        Numero : """)  
            if (opcion=="1") :
                fs.consulta_saldo()
            elif (opcion== "2"):
                a,b=fs.ingresar_y_actualizar()
                print("ïngrsar y actualizar: ")
            elif (opcion== "3"):
                a,b=fs.retirar_y_actualizar()
                print("retire su dinero:")
            elif (opcion== "4"):
                a,b=fs.salir()
                break
            else:
                print("ninguna opcion es correcta") 
    
    condicion=True    
    

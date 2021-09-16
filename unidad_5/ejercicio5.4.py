"""
Crear una funcion que debe:

*   Pedir al usuario una cantidad de tramos de un viaje
*   Pedir al usuario la duracion en minutos de cada tramo (usar listas)
*   Calcular el tiempo total de viaje (motrar en horas)
*   No deben aparecer y se deben tener en cuenta todos los posibles errores
"""
def tiempo_de_viaje():
    while True:
        try:
            while True:
                tramos=int(input("Ingrese el N° de Tramos: "))
                if tramos<=0:
                    print("Ingrese un numero mayor a 0.")
                else:
                    break
            tiempo_total_viaje=[]
            for i in range(1, tramos+1 ,1):
                while True:
                    duracion_tramo=int(input(f"Duracion del tramo N° {i}: "))
                    if duracion_tramo<0:
                        print("Ingrese un numero mayor o igual a 0.")
                    else:
                        break
                tiempo_total_viaje +=[duracion_tramo]
            horas, minutos = divmod(sum(tiempo_total_viaje), 60)
            if horas>0:
                print(f"La duración del viaje es de {horas}:{minutos}hs ")
                break
            else:
                print(f"La duración del viaje es de {minutos} minutos. ")   
                break
        except:
 
            print("Error - Ingrese solo Numeros Enteros y Positivos.")

tiempo_de_viaje()
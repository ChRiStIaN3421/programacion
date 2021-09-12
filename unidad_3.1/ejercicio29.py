"""
El programa debe:
*    Pedir al usuario una cantidad de tramos de un viaje
*    Pedir al usuario la duración en minutos de cada tramo
*    Calcular el tiempo total de viaje
*    No deben generar errores
"""
while True :
    try:
        while True:
            cantidad_de_tramos=int(input("ingrese cantidad de tramos : "))
            if(cantidad_de_tramos<=0):
                print("ingrese un numero mayor a cero")
            else:
                break    

        tiempo_total_viaje=0
        for i in range(cantidad_de_tramos):
            while True:
                tiempo_tramo=int(input(f"ingrese la duracion del  tramo {i+1}"))
                if(tiempo_tramo<0):
                    print("por favor ingrese un numero mayor o igual a cero")
                else:
                    tiempo_total_viaje +=tiempo_tramo  
                    break

        print("el tiempo total del viaje fue de :{round{tiempo_total_viaje/60}} horas  ")
        break 

    except:
        print("error en la variable ")        



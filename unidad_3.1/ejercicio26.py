"""
El programa debe:
*     Preguntar al usuario una cantidad a invertir
*     Preguntar al usuario el interés anual y el número de años
*     Mostrar por pantalla el capital obtenido en la inversión cada año que dura la inversión
"""
plazoFijo = float(input("Ingrese Valor a invertir: "))
porcentaje = float(input("Ingrese porcentaje de ganancia anual: "))
cantidadA=int(input("Cantidad de años a invertir: "))

for i in range(cantidadA):
   
    Ganancia = plazoFijo * porcentaje /100
    plazoFijo = plazoFijo + Ganancia
    print(f"Dinero Final: ${plazoFijo}")
"""
El programa debe:

Pedir al usuario 3 notas de 3 parciales diferentes
verificar que los ingresados sean correctos
En caso correcto imprimir el promedio
En caso contrario imprimir un error
"""
try:
    nota_1=float(input("ingrese su primer nota : "))
    nota_2=float(input("ingrese su segunda nota : "))
    nota_3=float(input("ingrese su tercer nota : "))
    sumas=(nota_1+nota_2+nota_3)/3
    print(f"la suma entre {nota_1}+{nota_2}+{nota_3}\n es promediada por:{sumas} ")
except:
    print("los datos ingrresados no son validos\nVuleva intentarlo...")    
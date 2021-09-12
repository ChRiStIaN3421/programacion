"""
- pedir dos datos por consola
- verificar que los dos datos sean numeros enteros
- en caso verdadero imprimir la suma de ambos
- en caso contrario imprimir error
"""
try:
   num_1=int(input ("ingrese algun numero:"))
   num_2=int(input("ingrese otro numeor :"))
   print(num_1+num_2)
except:
    print("error")   
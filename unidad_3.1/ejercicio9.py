flag=True 
while flag:
 try:
    numero_inicial=int(input("ingrese un numero inicial:"))
    numero_limite=int(input("ingrese un numero limite:"))
 except:
    print("dije un numero")    
 if (numero_inicial<numero_limite):    
  while numero_inicial<=numero_limite:
    print(numero_inicial)
    numero_inicial+=1
    flag=False
 else:
     print ("el numero inicial debe ser menor que le limite")

frase=input("por  favor ingrse una frase :")
letra=input("por favor ingrese la letra que quiere contar: ")
contador=0
for i in  frase :
    print(i,end="")
    if i==letra:
        contador+=1
print(f"el numero de veces de la letra :{letra} es {contador}")        

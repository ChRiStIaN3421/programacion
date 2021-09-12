flag= True
while flag:
 try:
    dato_numerico=int(input("ingrese un numero : "))
    flag=False
 except:
    print("error,ingrese de vuelta ")
multiplicador=1
while multiplicador<=10:
    print(f"{multiplicador} * {dato_numerico} = {multiplicador +dato_numerico }")
    multiplicador+=1       
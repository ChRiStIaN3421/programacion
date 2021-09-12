frase = input("Por favor ingrese una frase: ")
letra = input("Por favor ingrese la letra que quiere contar: ")
contador = 0

for i in frase:
  if i == letra:
    contador+=1

print(f"El numero de veces de la letra: {letra} es de  {contador}")
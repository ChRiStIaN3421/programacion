"""
Crear un prgrama que debe:
*    Contar con un stock de frutas y otro de verduras (El stock indica si venden o no esa fruta o verdura, no la cantidad) - dos listas que inician vacias
*    Contar con un menu y 3 funciones

      1. Agregar frutas o verduras al correspondiente stock (verificando que que sean nuevas)
      2. Consultar el stock de frutas o verduras
      3. Eliminar un elemento del stock
"""
verdura=[]
fruta=[]
frutas= "manzana","mandarina","frutilla","durazno"
while True:
      try:
            frutas= input("Ingrese una fruta : ")    
            if frutas== "manzana" or frutas == "mandarina" or frutas=="frutilla" or frutas=="durazno":  
                  break  
            else:
                  print("No contamos con es fruta por favor elija otra")
      except:
            print("error")
stock_de_fruta=[]
for i in frutas:
      stock_de_fruta==frutas
print(f"si contamos con esa fruta: su fruta es {frutas}")


verduras= "lechuga","papa","acelga","batata"
while True:
      try:
            verduras= input("Ingrese una verdura: ")
            if verduras== "lechuga" or verduras== "papa" or verduras=="acelga" or verduras=="batata":
                  break      
            else:
                  print("No contamos con esa verdura por favor elija otra")
      except:
                  print("error")
stock_de_verdura=[]
for i in verduras:
 stock_de_verdura==verduras
print(f"si contamos con esa verdura: su verdura es {verduras}")


while True:
    condicion=input(
    """
    Por favor ingrese una opcion :
    1. agregue una fruta o verdura al stock
    2. Consulte stock de fruta o verdura solicitada 
    3. Elimine algun elemento del stock
    4 - Salir
    Ingrese: """)
    if condicion=="1":
        while True:
         def agregue_al_stock():
            for i in range(stock_de_fruta or stock_de_verdura):
                  while True:
                        try:
                              agregue_al_stock= input(f'Ingrese nueva fruta  o verdura{i+1}: ')
                              stock_de_fruta or stock_de_verdura.append(agregue_al_stock)
                              break
                        except:
                              print("Ingrese un dato correcto por favor")

    elif condicion=="2":
        while True:
          def consulte_stock():
            for i in range(stock_de_fruta or stock_de_verdura):
                  while True:
                        try:
                              consulte_stock= input(f'Ingrese su condulta sobre el stock de fruta o verdura: ')
                              stock_de_fruta or stock_de_verdura.append(consulte_stock)
                              break
                        except:
                              print("Ingrese un dato correcto")

    elif condicion=="3":
    
            while True:
             def elimine_algun_elemento_del_stock():
                  for i in range(stock_de_fruta or stock_de_verdura):
                        while True:
                              try:
                                    elimine_algun_elemento_del_stock= input(f'si desea puede eliminar un elemnto del stock: ')
                                    stock_de_fruta or stock_de_verdura.pop(elimine_algun_elemento_del_stock)
                                    break
                              except:
                                    print("Ingrese un dato por favor")

    elif condicion=="4":
      break
    else:
      print("Opcion Incorrecta.")


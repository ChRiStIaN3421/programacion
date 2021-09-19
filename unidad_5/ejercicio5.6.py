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
def stock_fruta(frutas):
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
def stock_verdura(verduras):
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

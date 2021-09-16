"""
Crear una funcion que debe:

*    Pedir al usuario 5 materias (por ejemplo Matemáticas, Física, Química, Historia y Lengua)
*    Verficiar que sea un nombre correcto
*    Almacenar los nombres en una lista
*    Mostrar las materias en orden alfabetico
*    No deben aparecer y se deben tener en cuenta todos los posibles errores
"""
def ordenamiento_palabra():
    listas_materias=[]
    for i in range(5):
        materia=input("ingrese una materia: ")
        if not materia.isalpha():
            print("el dato ingresado es incorrecto")
            break
        else:
           listas_materias.append(materia)
        
        listas_materias.sort()
        print(f"el ordenamiento de las palabras es: {listas_materias}")       

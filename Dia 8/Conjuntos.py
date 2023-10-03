conjunto = {2,5,7,1,9,3}

#Para crear un conjunto vacío,
conjunto_vacio = set()

#Conversión de otros datos en conjuntos sobre cualquier iterable
#se extraen los valores únicos de otros tipos de datos
print(set("tito"))                                                      #Un String
print(set([1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5]))               #Una Lista
print(set(("TITO", "CARLOS", 'ALBERTO', 'ZUCCALA', 'TITO', 'ALBERTO'))) #Una Tupla
print(set({'manzana': 'rojo', 'plátano': 'amarillo', 'kiwi': 'verde'})) #Un Diccionario se extraen las claves, que, por definición, son únicas
print(set({2,5,7,1,9,3,3,3}))                                           #Un Conjunto
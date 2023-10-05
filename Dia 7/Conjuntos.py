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

print()

#Añadir un elemento, debemos utilizar la función add()
beatles = set(['Lennon', 'McCartney','Harrison','Starr'])
beatles.add('Best')
print(beatles)

#Borrar elementos, debemos utilizar la funcion remove()
beatles.remove('Best')
print(beatles)

#Longitud de un conjunto, usamos la función len()
print(len(beatles))

#Iterar sobre un conjunto
for beatle in beatles:
    print(beatle)

#Ordenando un conjunto, usamos la funcion sorted() porque sort() NO FUNCIONA
print(sorted(beatles)) #Obtenemos una Lista con los elementos ordenados ya que los conjuntos no mantienen un orden

#Teoría de conjuntos
A= {1,2}
B={2,3}

#Intersección
print(A.intersection(B))
#Unión
print(A.union(B))
#Diferencia
print(A.difference(B))
#Diferencia simétrica
print(A.symmetric_difference(B))
#Inclusión
A = {2, 4, 6, 8, 10}
B = {4, 6, 8}
print(B < A) #subconjunto
print(B<=A)
print(A> B)  #superconjunto
print(A>=B)

#Conjuntos por comprensión
#aquellos números enteros múltiplos de 3 en el rango (0, 20)
numeros = {numero for numero in range(0,20) if numero % 3 == 0}
print(numeros)

#Conjuntos inmutables
#Python ofrece la posibilidad de crear conjuntos inmutables haciendo uso de la función frozenset()
marcas = [1, 3, 2, 3, 1, 4, 2, 4, 5, 2, 5, 5, 3, 1, 4]
marcas = frozenset(marcas)
print(marcas)
#marcas.add(50)  NO es posible modificar un conjunto frozenset()

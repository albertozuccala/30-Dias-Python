######## Listas ######
#Lista: es una colección ordenada y cambiable (modificable). Permite miembros duplicados.


empty_list = list() # Esto es una lista vacia
print(len(empty_list)) # 0

empty_list = []
print(empty_list)

fruits = ['banana', 'orange', 'mango', 'lemon']                     # list of fruits
vegetables = ['Tomato', 'Potato', 'Cabbage','Onion', 'Carrot']      # list of vegetables
animal_products = ['milk', 'meat', 'butter', 'yoghurt']             # list of animal products
web_techs = ['HTML', 'CSS', 'JS', 'React','Redux', 'Node', 'MongDB'] # list of web technologies
countries = ['Finland', 'Estonia', 'Denmark', 'Sweden', 'Norway']

# Imprimo las listas y el tamaño
print('Fruits:', fruits)
print('Number of fruits:', len(fruits))
print('Vegetables:', vegetables)
print('Number of vegetables:', len(vegetables))
print('Animal products:',animal_products)
print('Number of animal products:', len(animal_products))
print('Web technologies:', web_techs)
print('Number of web technologies:', len(web_techs))
print('Number of countries:', len(countries))

print(type(fruits)) #Imprimo el tipo de dato que es la lista
print()
# Modifico una lista

fruits = ['banana', 'orange', 'mango', 'lemon'] 
first_fruit = fruits[0] # Podemos acceder al primer elemento por su indice
print("Primer elemento: ",first_fruit)      # banana
second_fruit = fruits[1]
print("Segundo elemento: ",second_fruit)     # orange
last_fruit = fruits[3]
print("Ultimo elemento: ",last_fruit) # lemon
print()
# Ultimo indice
last_index = len(fruits) - 1
last_fruit = fruits[last_index]

# Acceder a elementos
fruits = ['banana', 'orange', 'mango', 'lemon'] 
last_fruit = fruits[-1]
second_last = fruits[-2]
print("Ultimo elemento: ",last_fruit)       # lemon
print("Ante ultimo elemento: ",second_last)      # mango
print()

# Cortar elementos
fruits = ['banana', 'orange', 'mango', 'lemon'] 
all_fruits = fruits[0:4] # Devuelve todos los elementos de la lista
all_fruits = fruits[0:] # Si no establecemos donde parar, toma todo el resto
orange_and_mango = fruits[1:3] # No incluye el indice final
orange_mango_lemon = fruits[1:]
print(all_fruits)
print(orange_and_mango)
print(orange_mango_lemon)
print()

# Otra forma de lo anterior"
fruits = ['banana', 'orange', 'mango', 'lemon'] 
all_fruits = fruits[-4:] # devuelve todos los frutos
# esto también da el mismo resultado que el anterior
orange_and_mango = fruits[-3:-1] # no incluye el índice final
orange_mango_lemon = fruits[-3:]
print(orange_mango_lemon)
print()

# Modifico elementos
fruits = ['banana', 'orange', 'mango', 'lemon'] 
fruits[0] = 'Avocado' 
print(fruits)       #  ['avocado', 'orange', 'mango', 'lemon']
fruits[1] = 'apple'
print(fruits)       #  ['avocado', 'apple', 'mango', 'lemon']
last_index = len(fruits) - 1
fruits[last_index] = 'lime'
print(fruits[-1])        #  ['avocado', 'apple', 'mango', 'lime']


# Agregar elementos a una lista
#Para agregar un elemento al final de una lista existente, usamos el método append()
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.append('apple')
print(fruits)           # ['banana', 'orange', 'mango', 'lemon', 'apple']
fruits.append('lime')   # ['banana', 'orange', 'mango', 'lemon', 'apple', 'lime']
print(fruits)
print()

# Insertar elementos en una lista
#Podemos usar el método insert() para insertar un solo elemento en un índice específico en una lista.
# Tenga en cuenta que otros elementos se desplazan a la derecha. 
# Los métodos insert() toman dos argumentos: índice y un elemento para insertar.
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.insert(2, 'apple') # insert apple between orange and mango
print(fruits)           # ['banana', 'orange', 'apple', 'mango', 'lemon']
fruits.insert(3, 'lime')   # ['banana', 'orange', 'apple', 'lime', 'mango', 'lemon']
print(fruits)
print()

#Eliminación de elementos de una lista
#El método de eliminación elimina un elemento específico de una lista
fruits = ['banana', 'orange', 'mango', 'lemon', 'banana']
fruits.remove('banana')
print(fruits)  # ['orange', 'mango', 'lemon', 'banana'] - this method removes the first occurrence of the item in the list
fruits.remove('lemon')
print(fruits)  # ['orange', 'mango', 'banana']
print()

#Eliminación de elementos mediante Pop
#El método pop() elimina el índice especificado (o el último elemento si no se especifica el índice):
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.pop()
print(fruits)       # ['banana', 'orange', 'mango']

fruits.pop(0)
print(fruits)       # ['orange', 'mango']
print()

#Eliminación de elementos mediante Del
#La palabra clave del elimina el índice especificado y también se puede usar para eliminar elementos 
#dentro del rango del índice. También puede eliminar la lista por completo.
fruits = ['banana', 'orange', 'mango', 'lemon', 'kiwi', 'lime']
del fruits[0]
print(fruits)       # ['orange', 'mango', 'lemon', 'kiwi', 'lime']
del fruits[1]
print(fruits)       # ['orange', 'lemon', 'kiwi', 'lime']
del fruits[1:3]     # esto elimina los elementos entre los índices dados, ¡así que no elimina el elemento con el índice 3!
print(fruits)       # ['orange', 'lime']
del fruits
#print(fruits)       # Esto debería dar: NameError: name 'fruits' is not defined
print()


#Elementos de la lista de compensación
#El método clear() vacía la lista:
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.clear()
print(fruits)       # []
print()

#Copiar una lista
#Es posible copiar una lista reasignándola a una nueva variable de la siguiente forma: 
# lista2 = lista1. Ahora, list2 es una referencia de list1, cualquier cambio que hagamos 
# en list2 también modificará el original, list1. Pero hay muchos casos en los que no nos gusta
# modificar el original sino que nos gusta tener una copia diferente. 
# Una forma de evitar el problema anterior es usar copy().
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits_copy = fruits.copy()
print(fruits_copy)       # ['banana', 'orange', 'mango', 'lemon']
fruits.clear()
print(fruits)
print()

#Unir listas
#Hay varias formas de unir o concatenar dos o más listas en Python
#Operador SUMA
positive_numbers = [1, 2, 3, 4, 5]
zero = [0]
negative_numbers = [-5,-4,-3,-2,-1]
integers = negative_numbers + zero + positive_numbers
print(integers) # [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
fruits = ['banana', 'orange', 'mango', 'lemon']
vegetables = ['Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot']
fruits_and_vegetables = fruits + vegetables
print(fruits_and_vegetables ) # ['banana', 'orange', 'mango', 'lemon', 'Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot']
print()

#Unir usando el método extend() 
#El método extend() permite agregar una lista en una lista. Vea el ejemplo a continuación.
num1 = [0, 1, 2, 3]
num2 = [4, 5, 6]
num1.extend(num2)
print('Números:', num1) # Números: [0, 1, 2, 3, 4, 5, 6]
print()

negative_numbers = [-5,-4,-3,-2,-1]
positive_numbers = [1, 2, 3,4,5]
zero = [0]
negative_numbers.extend(zero)
negative_numbers.extend(positive_numbers)
print('Integers:', negative_numbers) # Integers: [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
print()

fruits = ['banana', 'orange', 'mango', 'lemon']
vegetables = ['Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot']
fruits.extend(vegetables)
print('Fruits and vegetables:', fruits ) # Fruits and vegetables: ['banana', 'orange', 'mango', 'lemon', 'Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot']
print()

#Contar elementos en una lista
#El método count() devuelve el número de veces que aparece un elemento en una lista:
fruits = ['banana', 'orange', 'mango', 'lemon']
print(fruits.count('orange'))   # 1

ages = [22, 19, 24, 25, 26, 24, 25, 24]
print(ages.count(24))           # 3
print()

#Encontrar el índice de un elemento
#El método index() devuelve el índice de un elemento de la lista:
fruits = ['banana', 'orange', 'mango', 'lemon']
print(fruits.index('orange'))   # 1
ages = [22, 19, 24, 25, 26, 24, 25, 24]
print(ages.index(24))           # 2, la primer ocurrencia
print()

#Invertir una lista
#El método reverse() invierte el orden de una lista.
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.reverse()
print(fruits) # ['lemon', 'mango', 'orange', 'banana']

ages = [22, 19, 24, 25, 26, 24, 25, 24]
ages.reverse()
print(ages) # [24, 25, 24, 26, 25, 24, 19, 22]
print()

#Clasificación de elementos de la lista
#Para ordenar listas, podemos usar el método sort() o las funciones integradas sorted(). 
#El método sort() reordena los elementos de la lista en orden ascendente y modifica la lista original.
#Si un argumento del método sort() reverse es igual a verdadero, ordenará la lista en orden descendente.

#sort(): este método modifica la lista original
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.sort()
print(fruits)  # ordenada en orden alfabetico, ['banana', 'lemon', 'mango', 'orange']

fruits.sort(reverse=True)
print(fruits) # ['orange', 'mango', 'lemon', 'banana']

ages = [22, 19, 24, 25, 26, 24, 25, 24]
ages.sort()
print(ages) #  [19, 22, 24, 24, 24, 25, 25, 26]

ages.sort(reverse=True)
print(ages) #  [26, 25, 25, 24, 24, 24, 22, 19]
print()

#sorted(): devuelve la lista ordenada sin modificar la lista original
fruits = ['banana', 'orange', 'mango', 'lemon']
print(sorted(fruits))   # ['banana', 'lemon', 'mango', 'orange']

# Reverse order
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits = sorted(fruits,reverse=True)
print(fruits)     # ['orange', 'mango', 'lemon', 'banana']
print()
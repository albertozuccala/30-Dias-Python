######## Listas ######

empty_list = list() # Esto es una lista vacia
print(len(empty_list)) # 0

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

# Modifico una lista

fruits = ['banana', 'orange', 'mango', 'lemon'] 
first_fruit = fruits[0] # Podemos acceder al primer elemento por su indice
print(first_fruit)      # banana
second_fruit = fruits[1]
print(second_fruit)     # orange
last_fruit = fruits[3]
print(last_fruit) # lemon
# Ultimo indice
last_index = len(fruits) - 1
last_fruit = fruits[last_index]

# Acceder a elementos
fruits = ['banana', 'orange', 'mango', 'lemon'] 
last_fruit = fruits[-1]
second_last = fruits[-2]
print(last_fruit)       # lemon
print(second_last)      # mango
print()

# Cortar elementos
fruits = ['banana', 'orange', 'mango', 'lemon'] 
all_fruits = fruits[0:4] # Devuelve todos los elementos de la lista
all_fruits = fruits[0:] # Si no establecemos donde parar, toma todo el resto
orange_and_
mango = fruits[1:3] # No incluye el indice final
orange_mango_lemon = fruits[1:]
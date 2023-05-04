#La cadena multilínea se crea usando comillas triples simples (''') o triples dobles (""").
multiline_string = '''Esto es una 
prueba de multilinea.
Tercera linea.'''
print(multiline_string)

# Otra forma
multiline_string = """Esto es una 
prueba de multilinea.
Tercera linea."""
print(multiline_string)

first_name = 'Alberto'
last_name = 'Zucca'
space = ' '
full_name = first_name  +  space + last_name
print(full_name) 


print('Dias\tTopics\tExercises') 
print('Dia 1\t3\t5')
print('Dia 2\t3\t5')
print('Dia 3\t3\t5')
print('Dia 4\t3\t5')

print('Este es el simbolo de barra invertida (\\)') 
print('\"Escribir una comilla doble dentro de una comilla simple\"') 

#En Python hay muchas formas de formatear cadenas. 
#En esta sección, cubriremos algunos de ellos. 
#El operador "%" se utiliza para formatear un conjunto de variables encerradas en una "tupla" 
#(una lista de tamaño fijo), junto con una cadena de formato, 
#que contiene texto normal junto con "especificadores de argumento", 
#símbolos especiales como "%s" , "%d", "%f", "%.número de dígitosf".

# Strings solos
first_name = 'Tito'
last_name = 'Zucca'
language = 'Python'
formated_string = 'Soy %s %s. Aprendo %s' %(first_name, last_name, language)
print(formated_string)

# Strings  y numeros
radius = 10
pi = 3.14
area = pi * radius ** 2
formated_string = 'El area de un circulo de radio %d es %.2f.' %(radius, area) 
print(formated_string) 

python_libraries = ['Django', 'Flask', 'NumPy', 'Matplotlib','Pandas']
formated_string = 'Los siguientes librerias son de python: %s' % (python_libraries)
print(formated_string) 

#Este formato se introdujo en la versión 3 de Python.
first_name = 'Tito'
last_name = 'Zucca'
language = 'Python'
formated_string = 'Soy {} {}. Aprendo {}'.format(first_name, last_name, language)
print(formated_string)


a = 4
b = 3
print('{} + {} = {}'.format(a, b, a + b))
print('{} - {} = {}'.format(a, b, a - b))
print('{} * {} = {}'.format(a, b, a * b))
print('{} / {} = {:.2f}'.format(a, b, a / b)) # limita a 2 digitos despues del decimal
print('{} % {} = {}'.format(a, b, a % b))
print('{} // {} = {}'.format(a, b, a // b))
print('{} ** {} = {}'.format(a, b, a ** b))


#Otro nuevo formato de cadena es la interpolación de cadenas, f-strings. 
#Las cadenas comienzan con f y podemos inyectar los datos en sus posiciones correspondientes.

formated_string = f'Soy {first_name} {last_name}. Aprendo {language}'
print(formated_string)

a = 4
b = 3
print(f'{a} + {b} = {a +b}')
print(f'{a} - {b} = {a - b}')
print(f'{a} * {b} = {a * b}')
print(f'{a} / {b} = {a / b:.2f}')
print(f'{a} % {b} = {a % b}')
print(f'{a} // {b} = {a // b}')
print(f'{a} ** {b} = {a ** b}')

#Desempaquetar caracteres
language = 'Python'
a,b,c,d,e,f = language 
print(a) # P
print(b) # y
print(c) # t
print(d) # h
print(e) # o
print(f) # n

#Acceso a caracteres en strings por índice
language = 'Python'
first_letter = language[0]
print(first_letter) # primera letra
second_letter = language[1]
print(second_letter) # segunda letra
last_index = len(language) - 1
last_letter = language[last_index]
print(last_letter) #ultima letra

#Si queremos comenzar desde el extremo derecho, 
# podemos usar la indexación negativa. -1 es el último índice.
language = 'Python'
last_letter = language[-1]
print(last_letter) # n
second_last = language[-2]
print(second_last) # o

#Cortar cadenas de Python, podemos dividir cadenas en subcadenas.
language = 'Python'
first_three = language[0:3] # comienza en cero y hasta 3 pero no incluye 3
print(first_three) #Pyt

last_three = language[3:6] # comienza en 3 y hasta 6 pero no incluye 6
print(last_three) # hon
# otra forma 
last_three = language[-3:]
print(last_three)   # hon
last_three = language[3:]
print(last_three)   # hon

#Invertir una cadena
saludo = 'Hola, como estas!'
print(saludo[::-1])

#Saltar caracteres al cortar
#Es posible omitir caracteres durante el corte pasando el argumento de paso al método de corte.
language = 'Albertito'
pto = language[0:10:2]
print(pto) #Abrio
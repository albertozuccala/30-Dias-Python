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
ejemplo = 'Hola, como estas!'
print(ejemplo[::-1])

#Saltar caracteres al cortar
#Es posible omitir caracteres durante el corte pasando el argumento de paso al método de corte.
ejemplo = 'Albertito'
pto = ejemplo[0:10:2]
print(pto) #Abrio

#Métodos de cadena

#capitalize (): Convierte el primer carácter de la cadena en letra mayúscula
ejemplo = 'esta es una oracion en minusculas'
print(ejemplo.capitalize())

#count(): Devuelve ocurrencias de subcadena en cadena, cuenta(subcadena, inicio=.., final=..). 
# El inicio es una indexación inicial para contar y el final es el último índice para contar.
ejemplo = 'thirty days of python'
print(ejemplo.count('y')) # Cuenta la cantidad de 'y' que hay en el string
print(ejemplo.count('y', 5, 14)) # Cuenta la cantidad de 'y' en el string pero desde la posicion 5 hasta la 14 
print(ejemplo.count('0')) 

#endswith(): Comprueba si una cadena termina con un final específico
ejemplo = 'thirty days of python'
print(ejemplo.endswith('on'))   # True
print(ejemplo.endswith('tion')) # False

#expandtabs (): Reemplaza el carácter de tabulación con espacios, 
# el tamaño de tabulación predeterminado es 8. Toma el argumento de tamaño de tabulación
ejemplo = 'thirty\tdays\tof\tpython'
print(ejemplo.expandtabs())   # 'thirty  days    of      python'
print(ejemplo.expandtabs(10)) # 'thirty    days      of        python'

#find(): Devuelve el índice de la primera aparición de una subcadena, si no se encuentra devuelve -1
ejemplo = 'thirty days of python'
print(ejemplo.find('y'))  # 16
print(ejemplo.find('tho')) # 17

#rfind(): Devuelve el índice de la última aparición de una subcadena, si no se encuentra devuelve -1
ejemplo = 'treinta días de python'
print(ejemplo.rfind('y')) # 5
print (ejemplo.rfind ('th')) # 1

#format (): Formatea la cadena en una salida más agradable
first_name = 'Alberto'
last_name = 'Zucca'
edad = 250
trabajo = 'ingeniero'
país = 'Argentina'
oracion = 'Soy {} {}. Soy un {}. Tengo {} años. Vivo en {}.'.format(first_name, last_name, trabajo, edad, país)
print(oracion) # Soy Alberto Zucca. tengo 250 años Yo soy un maestro. Yo vivo en Argentina.
oracion = f'Soy {first_name} {last_name}. Soy un {trabajo}. Tengo {edad} años. Vivo en {país}.'
print(oracion) # Soy Alberto Zucca. tengo 250 años Yo soy un maestro. Yo vivo en Argentina.


#index (): Devuelve el índice más bajo de una subcadena, los argumentos adicionales indican el índice inicial y final 
# (predeterminado 0 y longitud de cadena - 1). Si no se encuentra la subcadena, genera un valueError.
ejemplo = 'treinta días de python'
sub_cadena = 'py'
print (ejemplo.index (sub_cadena)) # 16
print (ejemplo.index (sub_cadena, 9)) # 16
print ()

#rindex(): Devuelve el índice más alto de una subcadena, los argumentos adicionales indican el índice inicial y final
# (predeterminado 0 y longitud de la cadena - 1)
ejemplo = 'treinta días de python'
sub_cadena = 'ei'
print (ejemplo.rindex (sub_cadena)) # 2
#print (ejemplo.rindex (sub_cadena, 9)) # error
print ()

#isalnum(): Comprueba el carácter alfanumérico
ejemplo = 'TreintaDíasPython'
print(ejemplo.isalnum()) # Verdadero

ejemplo = '30DíasPython'
print(ejemplo.isalnum()) # Verdadero

ejemplo = 'treinta días de python'
print(ejemplo.isalnum()) # Falso, el espacio no es un carácter alfanumérico

ejemplo = 'treinta días de python 2019'
print(ejemplo.isalnum()) # Falso
print ()

#isalpha(): Comprueba si todos los elementos de la cadena son caracteres alfabéticos (a-z y A-Z)
ejemplo = 'treinta días de python'
print(ejemplo.isalpha()) # Falso, el espacio se excluye una vez más
ejemplo = 'TreintaDíasPython'
print(ejemplo.isalpha()) # Verdadero
ejemplo = '123'
print(ejemplo.isalpha()) # Falso
print ()

#isdecimal(): Comprueba si todos los caracteres de una cadena son decimales (0-9)
ejemplo = 'treinta días de python'
print(ejemplo.isdecimal()) # Falso
ejemplo = '123'
print(ejemplo.isdecimal()) # Verdadero
print()

#isdigit(): Comprueba si todos los caracteres de una cadena son números (0-9 y algunos otros caracteres Unicode para números)
ejemplo = 'Treinta'
print(ejemplo.isdigit()) # Falso
ejemplo = '30'
print(ejemplo.isdigit()) # Verdadero
ejemplo = '\u00BD'
print(ejemplo.isdigit()) # Falso
print()

#isnumeric(): Comprueba si todos los caracteres de una cadena son números o están relacionados con números
#  (al igual que isdigit(), solo acepta más símbolos, como ½)
ejemplo = '10'
print(ejemplo.isnumeric()) # Verdadero
ejemplo = '\u00BD' # ½
print(ejemplo.isnumeric()) # Verdadero
ejemplo = '10.5'
print(ejemplo.isnumeric()) # Falso
print()

#isidentifier(): Busca un identificador válido; verifica si una cadena es un nombre de variable válido
ejemplo = '30DíasDePython'
print(ejemplo.isidentifier()) # Falso, porque comienza con un número
ejemplo = 'treinta_días_de_python'
print(ejemplo.isidentifier()) # Verdadero
print()


#join(): Devuelve una cadena concatenada
ejemplo = ['HTML', 'CSS', 'JavaScript', 'Reaccionar']
resultado = ' '.join(ejemplo)
print (resultado) # 'HTML CSS JavaScript Reaccionar'
print()

tecnología_web = ['HTML', 'CSS', 'JavaScript', 'Reaccionar']
resultado = '# '.join(tecnología_web)
print (resultado) # 'HTML# CSS# JavaScript# Reaccionar'
print()

#strip (): Elimina todos los caracteres dados desde el principio y el final de la cadena
ejemplo = 'treinta días de pythoonnn'
print(ejemplo.strip('noth')) # 'reinta días de py'
print()


#replace (): Reemplaza la subcadena con una cadena dada
ejemplo = 'treinta días de python'
print(ejemplo.replace('python', 'codificación')) # 'treinta días de codificación'
print()


#split (): Divide la cadena, utilizando la cadena dada o el espacio como separador
ejemplo = 'treinta días de python'
print(ejemplo.split()) # ['treinta', 'días', 'de', 'python']

ejemplo = 'treinta, días, de, python'
print(ejemplo.split(', ')) # ['treinta', 'días', 'de', 'python']
print()


#title (): Devuelve una cadena de título en mayúsculas
ejemplo = 'treinta días de python'
print(ejemplo.title()) # Treinta días de Python
print()

#swapcase (): Convierte todos los caracteres en mayúsculas a minúsculas 
# y todos los caracteres en minúsculas a caracteres en mayúsculas
ejemplo = 'treinta días de python'
print(ejemplo.swapcase()) # TREINTA DÍAS DE PYTHON
ejemplo = 'Treinta días de Python'
print(ejemplo.swapcase()) # tREINTA DÍAS DE pYTHON
print()

#startswith(): Comprueba si la cadena comienza con la cadena especificada
ejemplo = 'treinta días de python'
print(ejemplo.startswith('treinta')) # Verdadero
print()

ejemplo = '30 días de python'
print(ejemplo.startswith('treinta')) # Falso
print()

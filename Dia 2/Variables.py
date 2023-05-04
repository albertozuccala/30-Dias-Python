# Variables

'''''''''
help("keywords") #Imprime las palabras reservadas de python
help(str) #Muestra informacion de string
'''''''''

print(max(10,20,50,80,1)) #muestra el mayor valor
print(max([50,20,40,180,3])) #muestra el mayor valor de una lista


print('Hello, World!') # The text Hello, World! is an argument
print('Hello',',', 'World','!') # it can take multiple arguments, four arguments have been passed
print(len('Hello, World!')) # it takes only one argument



# Declaracion de Variables
first_name = 'Asabeneh'
last_name = 'Yetayeh'
country = 'Finland'
city = 'Helsinki'
age = 250
is_married = True
skills = ['HTML', 'CSS', 'JS', 'React', 'Python']
person_info = {
   'firstname':'Asabeneh',
   'lastname':'Yetayeh',
   'country':'Finland',
   'city':'Helsinki'
   }


#Usos de las variables
print('First name:', first_name)
print('First name length:', len(first_name))
print('Last name: ', last_name)
print('Last name length: ', len(last_name))
print('Country: ', country)
print('City: ', city)
print('Age: ', age)
print('Married: ', is_married)
print('Skills: ', skills)
print('Person information: ', person_info)


#Declaracion de variables en una misma linea
first_name, last_name, country, age, is_married = 'Asabeneh', 'Yetayeh', 'Helsink', 250, True

print(first_name, last_name, country, age, is_married)
print('First name:', first_name)
print('Last name: ', last_name)
print('Country: ', country)
print('Age: ', age)
print('Married: ', is_married)


#Obtener la entrada del usuario usando la función incorporada input()
'''
Nombre = input('Cual es su Nombre: ')
Edad = input('Cual es su Edad? ')
print(first_name)
print(age)
'''

#Casting
num_int = 10
num_float = 2.5
num_str = '10.1'
Nombre = 'Alberto'
print(float(num_int)) # int to float
print(int(num_float)) # float to int
print(str(num_int))   # int to str
#print(int(num_str))  # str to int no funciona
print(float(num_str)) # str to float
print(list(Nombre)) # str to list

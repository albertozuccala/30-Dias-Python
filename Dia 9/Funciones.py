#Retornando múltiples valores
#Una función puede retornar más de un valor. El «secreto» es hacerlo mediante una tupla
def multiple():
    return 0,1

print(multiple()) #Devuelve una tupla
print(type(multiple())) #El tipo es una tupla

#Por lo tanto, podremos aplicar el desempaquetado de tuplas sobre el valor retornado por la función
a,b = multiple()

print(a,b)

#Argumentos posicionales
def construir_cpu(vendor, num_cores, freq):
    return dict(
    vendor=vendor,
    num_cores=num_cores,
    freq=freq
    )

#es un mapeo directo entre argumentos y parámetros en el mismo orden que estaban definidos
print(construir_cpu("AMD", 8, 2.7)) 

#Argumentos nominales
print(construir_cpu(vendor="AMD", num_cores=8, freq=2.7))
#Se puede ver claramente que el orden de los argumentos no influye en el resultado final
print(construir_cpu( num_cores=8, vendor="AMD", freq=2.7))

#Argumentos posicionales y nominales
#los argumentos posicionales siempre deben ir antes que los argumentos nominales
print(construir_cpu("INTEL", num_cores=4, freq=3.1))


#Argumentos mutables e inmutables
valores = [6, 5, 4]


def raiz_cuadrada(valores):
    for i in range(len(valores)):
        valores[i] **=2
    return valores

#Esta función devuelve la raiz cuadrada de los elementos de la lista valores[]
#pero modifica su contenido internamente y no es lo correcto
print(raiz_cuadrada(valores))
print(valores)

#Parámetros por defecto
#En el caso de que no se proporcione un valor al argumento en la llamada a la función, el parámetro
#correspondiente tomará el valor definido por defecto.
def construir_cpu(vendor, num_cores, freq=2.0):
    return dict(
    vendor=vendor,
    num_cores=num_cores,
    freq=freq
    )

#Llamada a la función sin especificar frecuencia de «cpu»
print(construir_cpu("INTEL",2)) 

#Llamada a la función indicando una frecuencia concreta de «cpu»
print(construir_cpu("INTEL",2,4.45)) 

#Empaquetar/Desempaquetar argumentos posicionales
#Si utilizamos el operador * delante del nombre de un parámetro posicional, estaremos
#indicando que los argumentos pasados a la función se empaqueten en una tupla.
def _sum(*values: int) -> int:
    print(f'{values = }')
    result = 0
    for value in values: # values es una tupla
        result += value
    return result

print(_sum(4, 3, 2, 1))

# Desempaquetado: 
values = (4, 3, 2, 9)
print(_sum(*values))

#Empaquetar/Desempaquetar argumentos nominales
#Si utilizamos el operador ** delante del nombre de un parámetro nominal, estaremos
#indicando que los argumentos pasados a la función se empaqueten en un diccionario.
def mejor_estudiante(**notas: int) -> str:
    print(f'{notas = }')
    max_nota = 1
    for estudiante, nota in notas.items(): # notas es un diccionario
        if nota > max_nota:
            max_nota = nota
            mejor_estudiante = estudiante
    return mejor_estudiante

print(mejor_estudiante(ana=8, antonio=6, inma=9, javier=7))

# Desempaquetado:
print()
notas = dict(ana=8, antonio=6, inma=9, javier=7)
print(mejor_estudiante(**notas))


# Convenciones
#se utiliza args como nombre de parámetro para argumentos posicionales
#y kwargs como nombre de parámetro para argumentos nominales
def func(*args, **kwargs):

#Argumentos sólo nominales
#tendremos que incluir un parámetro especial * que delimitará el tipo de parámetros. 
# Así, todos los parámetros a la derecha del separador estarán obligados a ser nominales  

def sum_potencia(a, b, *, potencia=False):
    if potencia:
        a**= 2
        b**=2
    return a+b

print(sum_potencia(3, 4))

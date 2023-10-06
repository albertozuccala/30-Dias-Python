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
valores = [2, 3, 4]


def raiz_cuadrada(valores):
     for i in range(len(valores)):
          valores[i] **=2
          return valores


print(raiz_cuadrada(valores))
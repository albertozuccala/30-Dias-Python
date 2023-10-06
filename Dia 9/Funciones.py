#Retornando múltiples valores
#Una función puede retornar más de un valor. El «secreto» es hacerlo mediante una tupla
def multiple():
    return 0,1

print(multiple()) #Devuelve una tupla
print(type(multiple())) #El tipo es una tupla

#Por lo tanto, podremos aplicar el desempaquetado de tuplas sobre el valor retornado por la función
a,b = multiple()

print(a,b)

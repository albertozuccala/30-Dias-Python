rae = {
        "bifronte": "De dos frentes o dos caras",
        "anarcoide": "Que tiende al desorden",
        "montuvio": "Campesino de la costa"
       }


#print(rae["anarcoide"]) #Obtengo un elemento que existe
#print(rae.get("anarcoide")) #Obtengo un elemento con Get() para posibles claves que no existen
#print(rae.get("pepe")) #Devuelve NONE si no existe la clave
#print(rae.get("pepe","nada")) #Devuelve el valor que especificvo si no encuentra la clave en el dicc
 
rae["popo"] = "caca" #Agrego un elemento

rae["popo"] = "caca, solo caca" #Modifico un elemento

VOCALES = "aeiou"
enum_vocales = {} #Creacion de un diccionario desde vacio
for i, vocal in enumerate(VOCALES, start=1): #con enumerate() para los valores de las vocales
    enum_vocales[vocal] = i  #Lleno el diccionario con las vocales como clave y los numeros como los valores
    print(vocal,i)

print("a" in enum_vocales)  #Pertenencia de una clave en el dicc
print(rae.keys()) #Obtengo todas las claves del dicc con KEYS()
print(rae.values()) #Obtengo todos los valores del dicc con VALUES()
print(rae.items())  #Obtengo todos los pares clave-valor del dicc con ITEMS()
print(len(rae)) #Cuantos elementos tiene el dicc

#Como iterar un diccioanrio con su clave y valor
#De la misma forma se puede iterar con su clave o con su valor
for palabra, significado in rae.items():
    print(f'{palabra} : {significado}')


rae1 = {
        "combinar": "Una prueba de mezclar diccioanrios",
        "anarcoide": "No tengo idea",
        "montuvio": "Campesino de la costa"
    }
rae2 = {
        "bifronte": "De dos frentes o dos caras",
        "anarcoide": "Que tiende al desorden",
        "caca": "Caca, solo caca"
    }

#Combinar diccioanarios 
#Si la clave no existe, se añade con su valor.
#Si la clave ya existe, se añade con el valor del «último» diccionario en la mezcla
#Sin modificar los dicc originales con ** o |
print({**rae1, **rae2}) 
print(rae1 | rae2)
#Modificado los dicc originales
rae1.update(rae2)
print(rae1)

#Borrar elementos
#Por su clave con DEL()
del rae1["bifronte"]
print(rae1)
#Por su clave con POP (con extracción) podemos extraer un elemento
rae1.pop("anarcoide")
print()
print(rae1)
#Borrado completo del diccionario
rae1.clear()
print(rae1)

#Diccionarios por comprensión
palabras = ("hola", "como","te","va?","estas", "ahi?")
dicc_palabras = {palabra: len(palabra) for palabra in palabras}
print(dicc_palabras)

#También podemos aplicar condiciones a estas comprensiones
#Sólo mostrar palabras que tengan tamaño de 4
dicc_palabras = {palabra: len(palabra) for palabra in palabras if len(palabra) == 4}
print()
print(dicc_palabras)
print()

#Sólo mostrar palabras que empiecen por vocal
dicc_palabras = {palabra: len(palabra) for palabra in palabras if palabra[0] in ("a","e","i","o","u")}
print(dicc_palabras)

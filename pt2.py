def crear_diccionario(traducciones):
    diccionario = {}
    for par in traducciones.split(","):
        espan, glish = par.split(":")
        diccionario[espan.strip()] = glish.strip()
    return diccionario

def traducir_frase(diccionario, frase):
    palabras = frase.split()
    traduccion = []
    for palabra in palabras:
        traduccion.append(diccionario.get(palabra, palabra))  #Deja sin traducir si no está en el diccionario
    return " ".join(traduccion)

print("")
entradas = input("Introduce las traducciones (formato: palabra:traducción, ...): ")
diccionario_traduccion = crear_diccionario(entradas)

frase_espanol = input("Introduce una frase en español: ")
frase_traducida = traducir_frase(diccionario_traduccion, frase_espanol)

print("Traducción:", frase_traducida)
print("")
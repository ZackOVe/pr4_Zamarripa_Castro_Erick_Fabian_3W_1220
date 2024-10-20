print("")
print("Zamarripa Castro Erick Fabián 3W 1220")
print("")

# Creación de diccionario
pal = {
    'hola': 'hello',
    'agua': 'water',
    'adios': 'goodbye',
    'fuego': 'fire',
    'perro': 'dog',
    'gato': 'cat',
}

# El usuario escribirá la palabra en español
a = input("Ingrese una palabra (Español): ").strip().lower()

# Si "a" está disponible
if a in pal:
    tra = pal[a]
    # Imprimirá la traducción
    print("La palabra", a, "es", tra, "en inglés")
else:
    print("Esa palabra no está disponible")

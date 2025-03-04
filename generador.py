import random
import string

def generar_contraseña(longitud, usar_mayus, usar_minus, usar_numeros, usar_especiales):
    caracteres = ""
    if usar_mayus:
        caracteres += string.ascii_uppercase
    if usar_minus:
        caracteres += string.ascii_lowercase
    if usar_numeros:
        caracteres += string.digits
    if usar_especiales:
        caracteres += string.punctuation

    if not caracteres:
        print("Debes seleccionar al menos un tipo de caracter. Se usarán todos por defecto.")
        caracteres = string.ascii_letters + string.digits + string.punctuation

    contraseña = ''.join(random.choice(caracteres) for _ in range(longitud))
    return contraseña

# Pedir al usuario la longitud de la contraseña
try:
    longitud = int(input("Introduce la longitud de la contraseña (mínimo 8): "))
    if longitud < 8:
        print("La longitud mínima es 8. Se usará 8 caracteres.")
        longitud = 8
except ValueError:
    print("Entrada no válida. Se usará una longitud de 12.")
    longitud = 12

# Pedir al usuario qué tipos de caracteres incluir
usar_mayus = input("¿Incluir mayúsculas? (s/n): ").strip().lower() == "s"
usar_minus = input("¿Incluir minúsculas? (s/n): ").strip().lower() == "s"
usar_numeros = input("¿Incluir números? (s/n): ").strip().lower() == "s"
usar_especiales = input("¿Incluir caracteres especiales? (s/n): ").strip().lower() == "s"

# Generar y mostrar la contraseña
contraseña_generada = generar_contraseña(longitud, usar_mayus, usar_minus, usar_numeros, usar_especiales)
print(f"\nTu contraseña generada es: {contraseña_generada}")
import random
import string
import streamlit as st

# Función para generar la contraseña
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
        st.warning("Debes seleccionar al menos un tipo de carácter. Se usarán todos por defecto.")
        caracteres = string.ascii_letters + string.digits + string.punctuation

    contraseña = ''.join(random.choice(caracteres) for _ in range(longitud))
    return contraseña

# Interfaz de usuario en Streamlit
st.title("Generador de Contraseñas Aleatorias")

# Pedir al usuario la longitud de la contraseña
longitud = st.number_input("Introduce la longitud de la contraseña (mínimo 8):", min_value=8, value=12)

# Pedir al usuario qué tipos de caracteres incluir
usar_mayus = st.checkbox("Incluir mayúsculas", value=True)
usar_minus = st.checkbox("Incluir minúsculas", value=True)
usar_numeros = st.checkbox("Incluir números", value=True)
usar_especiales = st.checkbox("Incluir caracteres especiales", value=True)

# Botón para generar la contraseña
if st.button("Generar Contraseña"):
    contraseña_generada = generar_contraseña(longitud, usar_mayus, usar_minus, usar_numeros, usar_especiales)
    st.subheader("Tu contraseña generada es:")
    st.write(contraseña_generada)

import streamlit as st
import hashlib

# Función para hashear contraseñas
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Base de datos de usuarios con contraseñas hash (puedes agregar más)
USER_DATA = {
    "usuario1": hash_password("password123"),
    "usuario2": hash_password("miClaveSegura"),
}

# Función de autenticación
def login(username, password):
    if username in USER_DATA and USER_DATA[username] == hash_password(password):
        return True
    return False

def set_cookie(key, value):
    st.session_state[key] = value

# Interfaz de inicio de sesión
def login_screen():
    st.title("Iniciar Sesión")
    username = st.text_input("Usuario")
    password = st.text_input("Contraseña", type="password")
    if st.button("Login"):
        if login(username, password):
            set_cookie('user', username)
            return True
        else:
            st.error("Usuario o contraseña incorrectos")
    return False

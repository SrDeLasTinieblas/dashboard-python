import streamlit as st
import pandas as pd
import numpy as np
from auth import login_screen
from openpyxl import Workbook
from openpyxl.drawing.image import Image
from openpyxl.utils.dataframe import dataframe_to_rows
import datetime, time
from dashboard import mostrar_dashboard

def get_cookie(key):
    return st.session_state.get(key, None)

# Verificar si el usuario está autenticado
if 'authenticated' not in st.session_state:
    st.session_state.authenticated = False

if not st.session_state.authenticated:
    # Mostrar pantalla de inicio de sesión si no está autenticado
    if login_screen():
        st.session_state.authenticated = True
        st.session_state.redirecting = True  # Añadir indicador de redirección
        # Mostrar un mensaje de carga antes de mostrar el dashboard
        with st.spinner("Redirigiendo al dashboard..."):
            time.sleep(3)  # Esperar 3 segundos    
        st.session_state.redirecting = False  # Terminar redirección
else:
    username = get_cookie('user')
    success_message = st.success(f"Bienvenido {username}")
    time.sleep(3)    
    success_message.empty()    
    mostrar_dashboard()

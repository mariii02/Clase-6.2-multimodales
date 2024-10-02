import streamlit as st
import cv2
import numpy as np
import pytesseract
from PIL import Image

# Título de la aplicación
st.title("📸 Reconocimiento Óptico de Caracteres (OCR)")

# Captura de imagen
img_file_buffer = st.camera_input("Toma una Foto")

# Sidebar para opciones de filtro
with st.sidebar:
    st.header("Opciones")
    filtro = st.radio("Aplicar Filtro:", ('Con Filtro', 'Sin Filtro'))

# Procesar la imagen si se ha capturado
if img_file_buffer is not None:
    # Leer el buffer de la imagen con OpenCV
    bytes_data = img_file_buffer.getvalue()
    cv2_img = cv2.imdecode(np.frombuffer(bytes_data, np.uint8), cv2.IMREAD_COLOR)

    # Aplicar filtro según la selección
    if filtro == 'Con Filtro':
        cv2_img = cv2.bitwise_not(cv2_img)  # Inversión de colores

    # Convertir la imagen a RGB para mostrarla
    img_rgb = cv2.cvtColor(cv2_img, cv2.COLOR_BGR2RGB)
    
    # Mostrar la imagen procesada
    st.image(img_rgb, caption="Imagen Procesada", use_column_width=True)

    # Reconocimiento de texto
    text = pytesseract.image_to_string(img_rgb)
    
    # Mostrar el texto reconocido
    st.subheader("Texto Reconocido:")
    st.write(text) 

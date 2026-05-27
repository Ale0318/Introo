import streamlit as st

# TITULO
st.title("Mood Space")

# SUBTITULO
st.header("Mi primera app interactiva 💗")

# TEXTO
st.subheader(
    "En este espacio exploro emociones, creatividad y experiencias multimodales."
)

st.write(
    "Las interfaces multimodales permiten combinar imágenes, texto, audio e interacción para mejorar la experiencia del usuario."
)

# IMAGEN
st.image("intro.jpg", width=350)

# INPUT
texto_usuario = st.text_input(
    "Describe tu mood del día"
)

st.write("Tu mood actual es:", texto_usuario)

# SEPARADOR
st.divider()

# COLUMNAS
col1, col2 = st.columns(2)

###################################################
# COLUMNA 1
###################################################

with col1:

    st.header("Experiencia Visual")

    st.write(
        "Las imágenes y colores ayudan a transmitir emociones dentro de una interfaz."
    )

    acuerdo = st.checkbox("Estoy de acuerdo")

    if acuerdo:
        st.write("Las experiencias visuales hacen la interfaz más atractiva.")

###################################################
# COLUMNA 2
###################################################

with col2:

    st.header("Modalidad Favorita")

    opcion = st.radio(
        "¿Qué modalidad prefieres?",
        ("Visual", "Auditiva", "Táctil")
    )

    if opcion == "Visual":
        st.write("La vista es fundamental para tu experiencia.")

    elif opcion == "Auditiva":
        st.write("El sonido mejora la interacción.")

    else:
        st.write("La interacción física hace todo más inmersivo.")

# SEPARADOR
st.divider()

###################################################
# BOTON
###################################################

st.header("Interacción")

if st.button("Presiona aquí"):

    st.success("Gracias por interactuar con Mood Space")

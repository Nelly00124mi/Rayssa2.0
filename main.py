import streamlit as st
import pandas as pd

st.title("Bloco de notas🔠")
st.snow()

# Exibe o campo de entrada de chat
mensagem = st.chat_input("Digite suas notas a serem armazenadas aqui...")

# Verifica se o usuário enviou algo
if mensagem:
    st.write(f"Você : {mensagem}")

    
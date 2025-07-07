import streamlit as st
import pandas as pd

st.title("Bloco de notas🔠")
st.button("Balões")
st.balloons

# Exibe o campo de entrada de chat
mensagem = st.chat_input("Digite suas notas a serem armazenadas aqui...")

# Verifica se o usuário enviou algo
if mensagem:
    st.write(f"Você : {mensagem}")

    
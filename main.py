import streamlit as st
import pandas as pd

st.title("Perguntas sobre você🐹")

# Exibe o campo de entrada de chat
mensagem = st.chat_input("Digite sua mensagem aqui...")

# Verifica se o usuário enviou algo
if mensagem:
    st.write(f"Você : {mensagem}")
import streamlit as st
import pandas as pd

# Configurações da página
st.set_page_config(page_title="Chat Online", layout="centered")
st.title("💬 Chat Simples com Streamlit")

# Inicializar o histórico se ainda não existir
if "mensagens" not in st.session_state:
    st.session_state.mensagens = []

# Exibir as mensagens anteriores
for msg in st.session_state.mensagens:
    with st.chat_message(msg["autor"]):
        st.markdown(msg["texto"])

# Entrada de mensagem
entrada = st.chat_input("Digite sua mensagem...")

# Processar nova mensagem
if entrada:
    # Adicionar mensagem do usuário ao histórico
    st.session_state.mensagens.append({"autor": "user", "texto": entrada})
    
    # Mostrar mensagem enviada
    with st.chat_message("user"):
        st.markdown(entrada)

    # Resposta automática (simples)
    resposta = f"Você disse: '{entrada}'. Que interessante!"
    st.session_state.mensagens.append({"autor": "assistant", "texto": resposta})

    # Mostrar resposta
    with st.chat_message("assistant"):
        st.markdown(resposta)


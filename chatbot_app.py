import streamlit as st
import os
from mistralai import Mistral




def generate_response(user_input):
    api_key = "9F8Lnhk8zfkxKxj3EfCyY3j9RzIaVwjB"
    model = "mistral-large-latest"
    client = Mistral(api_key=api_key)

    chat_response = client.chat.complete(
        model = model,
        messages = [
            {
                "role": "user",
                "content": user_input,
            },
        ]
    )
    return chat_response.choices[0].message.content


st.title("Chatbot avec Streamlit")
st.write("Bienvenue sur l'interface de chatbot. Posez-moi des questions !")
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

with st.form(key='chat_form', clear_on_submit=True):
    user_input = st.text_input("Vous :", key="input")
    submit_button = st.form_submit_button(label='Envoyer')

demande_generale = "reponds moi en espagnol"

#generate_response(demande_generale)

if submit_button and user_input:
    response = generate_response(demande_generale + user_input)
    # Ajouter l'entrée utilisateur et la réponse à l'historique
    st.session_state.chat_history.append(("Vous", user_input))
    st.session_state.chat_history.append(("Bot", response))

# Affichage de l'historique des échanges
for sender, message in st.session_state.chat_history:
    if sender == "Vous":
        st.write(f"**{sender}:** {message}")
    else:
        st.write(f"*{sender}:* {message}")



import streamlit as st
import ollama
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

MODEL = os.getenv("OLLAMA_MODEL", "llama3.2")

st.title("My Ollama Chatbot")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User input
if prompt := st.chat_input("Ask me anything..."):

    st.session_state.messages.append({
        "role": "user",
        "content": prompt
    })

    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = ollama.chat(
                model=MODEL,
                messages=st.session_state.messages
            )

            answer = response["message"]["content"]
            st.markdown(answer)

    st.session_state.messages.append({
        "role": "assistant",
        "content": answer
    })

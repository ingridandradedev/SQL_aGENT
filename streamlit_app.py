import streamlit as st
import requests

st.title("🔎SQL AI Agent")

"""
Oi! Sou um agente SQL especializado em explorar dados de marketing e redes sociais. 
Comigo, você consegue insights valiosos sobre engajamento, performance e orçamento das suas campanhas.
"""

# Initialize session state for storing chat history
if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "Olá, o que você quer saber sobre sua campanhas hoje?"}]

# Display chat messages from session state
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input("Digite uma mensagem:"):
    # Display user message in chat
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Send request to the updated Langflow API
    try:
        headers = {
            "Content-Type": "application/json",
            "Authorization": "Bearer sk-0EDDDAlNjRscbzqGZtDVsalsBvW52niFZ_2qfpQn-Xk"
        }
        data = {
            "input_value": prompt,
            "output_type": "chat",
            "input_type": "chat",
            "tweaks": {
                "OpenAIToolsAgent-a5UmQ": {},
                "ChatInput-fQPzn": {},
                "ChatOutput-kXBtP": {},
                "OpenAIModel-MCktn": {},
                "SupabaseSQLTool-L7eo1": {},
                "Memory-Zlwnh": {},
                "Prompt-PxHif": {}
            }
        }

        response = requests.post(
            "https://langflowailangflowlatest-production-74ad.up.railway.app/api/v1/run/sql-agent-for-marketing?stream=false",
            headers=headers,
            json=data
        )
        response_data = response.json()

        # Extract the assistant's response
        assistant_message = response_data["outputs"][0]["outputs"][0]["results"]["message"]["data"]["text"]

        # Display assistant message in chat
        with st.chat_message("assistant"):
            st.markdown(assistant_message)

        # Add assistant message to chat history
        st.session_state.messages.append({"role": "assistant", "content": assistant_message})

    except Exception as e:
        st.error(f"Erro: {e}")

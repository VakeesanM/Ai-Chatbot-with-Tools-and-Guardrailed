import streamlit as st
from chatbot.bot import ChatBot

st.set_page_config(page_title="Chatbot with Guardrails", page_icon='🤖')
st.header("Chatbot with Guardrails - Demo!")
st.write("This Chatbot agent has memory and guardrails. It can deal with PII info(Credit Card, IP, and Email) and guardrails that can deal with prompt injection to a minor level")
st.write("It also has a few tools, allowing it solve math problems as well surf the web")

if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "AI", "content": "Hi, how can I help you today?"}]
    st.session_state.chatbot = ChatBot()


for message in st.session_state.messages:
    with st.chat_message(message['role']):
        st.markdown(message['content']) 


if prompt := st.chat_input("How is it going?"):
    with st.chat_message('user'):
        st.markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    
    with st.chat_message("AI"):
        response = st.write_stream(st.session_state.chatbot.stream(prompt))

    st.session_state.messages.append({"role": "AI", "content": f"{response}"})

    



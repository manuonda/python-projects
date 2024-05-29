#pip install langchain streamlit lanchain-openai

import streamlit as st
from langchain_core.messages import AIMessage,HumanMessage

def get_response(user_input):
    return "I don't know"


#app config
st.set_page_config(page_title="Chat wit Websites")
st.title("Chat with websites")


#save the session and history chat
if "chat_history"  not in st.session_state: 
    st.session_state.chat_history = [
    AIMessage(content="Hello, I'm a bot.How can I help you?")
    ]

# sidebar
with st.sidebar:
    st.header("Settings")
    website_url = st.text_input("Website URL")

#user_input
user_query = st.chat_input("Type your message here")
if user_query is not None and user_query != "":
    response = get_response(user_query)
    st.session_state.chat_history.append(HumanMessage(content=user_query))
    st.session_state.chat_history.append(AIMessage(content=response))
    
with st.sidebar:
    st.write(st.session_state.chat_history)
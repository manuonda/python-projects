#pip install langchain streamlit lanchain-openai beautifulsoup4 python-dotenv

import streamlit as st
from langchain_core.messages import AIMessage,HumanMessage
from langchain_community.document_loaders import WebBaseLoader
from langchain.text_splitter import RecursiveTextSplitter
from lanchain_community.vectorstores import Chroma
from langchain_openai import OpeanAIEmbbedings, ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate, MessagePlaceHolder
from langchain.chains import create_history_aware_retriever


load_dotenv()

def get_response(user_input):
    return "I don't know"



## Function load url , read the content and split in chunks
## create a vectorstor from the chunkcs in the embeddings
def get_vectorstore_from_url(url):
    loader= WebBaseLoader(url)
    document = loader.load()
    
    #split the document in chunks
    text_spliter = RecursiveTextSplitter()
    document_chunks = text_spliter.split(document.text)
    
    #create a vectorstore from the chunks the embeddings to use is OpenAI
    vectorstore = Chroma.from_documents(document_chunks, OpeanAIEmbbedings())
    
    return document_chunks

def get_context_retriever_chain(vector_store):
    llm = ChatOpenAI()
    retriever = vector_store.as_retriever()
    prompt = ChatPromptTemplate.from_messages([
       MessagePlaceHolder(variable_name="chat_history"),
       ("user","{input}"),
       ("user", "Given the above conversation, generate a search query to look up in order to get information relevant to the conversation") 
    ])
    
    retriever_chain = create_history_aware_retriever(llm, retriever, prompt)


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

if website_url is None or website_url == "":
    st.info("Please enter a website URL")
else:
   document_chunks = get_vectorstore_from_url(website_url) 
   with st.sidebar:
       st.write(document_chunks)
       
   #user_input
   user_query = st.chat_input("Type your message here")
   if user_query is not None and user_query != "":
       response = get_response(user_query)
       st.session_state.chat_history.append(HumanMessage(content=user_query))
       st.session_state.chat_history.append(AIMessage(content=response))
       
   #conversation 
   for message in st.session_state.chat_history:
       if isinstance(message, AIMessage):
           with st.chat_message("AI"):
               st.write(message.content)
       elif isinstance(message, HumanMessage):
           with st.chat_message("Human"):
               st.write(message.content)
   
   
   with st.sidebar:
    st.write(st.session_state.chat_history)


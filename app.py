import streamlit as st 
import requests

st.title('chatbot')

if "conversation" not in st.session_state:
    st.session_state['conversation'] = []
    

    
prompt = st.chat_input('type your message')

if prompt:
    st.session_state['conversation'].append({"role":"user","data":prompt})
    response = requests.post(url="https://chakravardhan06.app.n8n.cloud/webhook/4da0711d-df72-4a5a-b69d-a29143a99874",
                  json={"prompt":prompt})
    
    if response.status_code == 200:
        st.session_state['conversation'].append({"role":"ai","data":response.json()['output']})
        #st.session_state['conversation'].append(response.json()['output'])
    
for con in st.session_state['conversation']:
    with st.chat_message(con['role']):
        st.write(con['data'])

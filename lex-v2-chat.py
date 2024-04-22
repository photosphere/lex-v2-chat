import os
import streamlit as st
import boto3
import json

lex_client = boto3.client("lexv2-runtime")

def get_res_from_lex(question):
    message=""
    try:
        response = lex_client.recognize_text(
            botId=os.environ["bot_id"],
            botAliasId=os.environ["bot_alias_id"],
            localeId=os.environ["locale_id"],
            sessionId='8faf613b-c281-4782-8fd7-0b97a589f22c',
            text=question)
        message = response['messages'][0]['content']
    except Exception as e:
            st.error('Lex Query Failed')
    return message

st.set_page_config(page_title="Lex Bot Test Tool!", layout="wide",page_icon=":speech_balloon:")   
st.title("Lex Bot Test Tool!")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# React to user input
if prompt := st.chat_input("请输入您的问题?"):
    # Display user message in chat message container
    st.chat_message("user").markdown(prompt)
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

    response = get_res_from_lex(prompt)
    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        st.markdown(response)
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})

with st.sidebar:

    bot_id_val=""
    bot_alias_id_val=""
    locale_id_val=""
    if os.path.exists('lex.json'):
        with open('lex.json') as f:
            data = json.load(f)
            bot_id_val = data['bot_id']
            bot_alias_id_val = data['bot_alias_id']
            locale_id_val = data['locale_id']

    bot_id = st.text_input('bot-id',value=bot_id_val)
    bot_alias_id = st.text_input('bot-alias-id',value=bot_alias_id_val)
    locale_id = st.text_input('locale-id',value=locale_id_val)

    st.write('*You must click follow button to save configuration of Lex Bot*')

    # save env
    if st.button('Save Configuration'):
        os.environ["bot_id"] = bot_id
        os.environ["bot_alias_id"] = bot_alias_id
        os.environ["locale_id"] = locale_id

        data = {
            "bot_id": bot_id,
            "bot_alias_id": bot_alias_id,
            "locale_id": locale_id
        }

        with open("lex.json", "w") as file:
            json.dump(data, file)

        st.success("ENV has been set")

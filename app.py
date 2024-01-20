import streamlit as st
from transformers import pipeline, Conversation


st.markdown("# Hi! I'm a chatbot")
st.markdown("##### I'm completely free, so don't expect too much from me :)")

if "chat" not in st.session_state:
    st.session_state.chat = Conversation()


@st.cache_resource()
def get_chatbot():
    return pipeline(model="facebook/blenderbot_small-90M")


chat = st.session_state.chat

with st.spinner("Loading chatbot..."):
    chatbot = get_chatbot()
for message in chat:
    with st.chat_message(message["role"].replace("assistant", "bot")):
        st.markdown(message["content"])

usr_msg = st.chat_input("Talk to me:)")

if usr_msg:
    with st.chat_message("user"):
        st.markdown(usr_msg)
        chat.add_message(dict(content=usr_msg, role="user"))
    with st.chat_message("bot"):
        with st.spinner("Typing..."):
            conversation = chatbot(chat)
            response = conversation.messages[-1]["content"]
        st.markdown(response)
        st.session_state.chat = chat

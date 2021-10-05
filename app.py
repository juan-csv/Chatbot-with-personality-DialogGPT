import streamlit as st
import inference_rick_app
import base64


def conver_image_in_url(path_im):
    file_ = open(path_im, "rb")
    contents = file_.read()
    data_url = base64.b64encode(contents).decode("utf-8")
    file_.close()
    return data_url

#create cache object for the "chat"
@st.cache(allow_output_mutation=True)
def Chat():
    return []

# Instance Bot
Rick_bot = inference_rick_app.Bot_rick()

# create object to sotrage messages
messages_history = Chat()


# create a sidebar for select Bot
bot_value = st.sidebar.radio(label="Select Character:", options=["Rick Sanchez", "Yoda", "Batman"])

# Rick Sanchez bot
if bot_value == "Rick Sanchez":
    # Load gif of Rick
    # transform gif in url for shows with markdown
    data_url = conver_image_in_url("content/Rick.gif")
    st.markdown(f"<img src='data:image/gif;base64,{data_url}' width='300'>",
    unsafe_allow_html=True)

    #
    st.text("")
    # Display History chat
    history_chat = st.empty()
    # Input text
    current_message = st.text_area("", value=f"Hello {bot_value}, how are you?")

    if st.button("Send"):
        # Add user response to History 
        messages_history.append(current_message)

        # Response bot
        response = Rick_bot.get_response(messages_history)

        # Add bot response to History
        messages_history.append(response) 

        # format message:
        Res = []
        for i,res in enumerate(messages_history):
            if i%2==0: # User
                Res.append(f">> User: {res}\n ")
            else: # Bot
                Res.append(f">> Rick bot: {res}\n ")
        
        # Show history chat                
        history_chat.text("".join(Res))


# TODO: enviar input text usando text_area
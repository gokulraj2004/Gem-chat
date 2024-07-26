import os

import streamlit as st
from dotenv import load_dotenv
import google.generativeai as gen_ai

#loading environment variable
load_dotenv()

#configuring streamlit page settings
st.set_page_config(
    page_icon='⭐',
    page_title='💎GemChat💎',
    layout='wide',
    menu_items={'Get Help': 'https://www.linkedin.com/in/gokulraj075/',
                'Report a bug': "https://www.linkedin.com/in/gokulraj075/",
                'About': "GOKUL RAJ.S | Junior Data Scientist | Proficient in Power BI, Advanced SQL, Python | Excel Expert | AZ-104 Certified | AZ-900 Certified | Google Cloud Certified 17+ Badges | Machine Learning | VIT 25"}
)



google_api=os.getenv("GOOGLE_API_KEY")

#Set up Google Gemini-Pro AI Model
gen_ai.configure(api_key=google_api)
model=gen_ai.GenerativeModel('gemini-pro')

#funcction to translate roles b/w gemini-pro and streamlit terminology
def translate_role_for_streamlit(user_role):
    if user_role=="model":
        return "assitant"
    else:
        return user_role

# Initialize chat session in streamlit if not already present
if "chat_session" not in st.session_state:
    st.session_state.chat_session = model.start_chat(history=[])
    
#Display the chatbot's title on the page
st.title("GemChat")
st.write("  𝖠 𝖼𝗁𝖺𝗍𝖻𝗈𝗍 𝖻𝗎𝗂𝗅𝗍 𝗐𝗂𝗍𝗁 𝖲𝗍𝗋𝖾𝖺𝗆𝗅𝗂𝗍, 𝗎𝗌𝗂𝗇𝗀 𝗍𝗁𝖾 𝖦𝖾𝗆𝗂𝗇𝗂 𝖠𝖯𝖨 𝗄𝖾𝗒 𝖿𝗈𝗋 𝗂𝗇𝗍𝖾𝗅𝗅𝗂𝗀𝖾𝗇𝗍 𝖺𝗇𝖽 𝗋𝖾𝗌𝗉𝗈𝗇𝗌𝗂𝗏𝖾 𝗂𝗇𝗍𝖾𝗋𝖺𝖼𝗍𝗂𝗈𝗇𝗌.")

col1, col2 = st.columns([4, 1])

with col1:
        st.subheader("") 
with col2:
        st.subheader("Gokul Raj")
        st.write("Junior Data Scientist | Proficient in Power BI, Advanced SQL, Python | Excel Expert | AZ-104 & AZ-900 Certified | Google Cloud Certified with 17+ Badges | Machine Learning Enthusiast | VIT 2025") 
        #add_predictions(input_data)



#Display the chatbot history
for message in st.session_state.chat_session.history:
    with st.chat_message(translate_role_for_streamlit(message.role)):
        st.markdown(message.parts[0].text)
        
#input field for user's message
user_prompt=st.chat_input("Ask Gemini....")
if user_prompt:
    # Add user's message to chat and display it
    st.chat_message("user").markdown(user_prompt)
    
    #send user's message to gemini and get the response
    gem_resp=st.session_state.chat_session.send_message(user_prompt)

    #Display Gemini response
    with st.chat_message("assistant"):
        st.markdown(gem_resp.text)
        

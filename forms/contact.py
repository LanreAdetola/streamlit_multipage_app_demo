import re
import requests
import streamlit as st
 
WEBHOOK_URL = st.secrets["WEBHOOK_URL"]

def is_valid_email(email):
    email_pattern = r"^[a-zA-Z0-9.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return re.match(email_pattern, email) is not None

def contact_form():
    with  st.form("contact_form"):
        name = st.text_input("First Name")
        email = st.text_input("Email Address")
        message = st.text_area("Your Message")
        submit_button = st.form_submit_button("Submit")

        if submit_button:
            if not WEBHOOK_URL:
                st.error("Email service not set up. Please try again")
                st.stop()
            
            if not name:
                st.error("Please provide your name")
                st.stop()

            if not email:
                st.error("Please provide your email")
                st.stop()

            if not is_valid_email(email):
                st.error("Please provide a valid email address")
                st.stop()

            if not message:
                st.error("Please provide your message")
                st.stop()

            #-- data payload-- 
            data = {"email": email, "name": name,  "message": message}
            response = requests.post(WEBHOOK_URL, json=data)

            if response.status_code == 200:
                st.success("Message succesfully sent!")
            else:
                st.error("There was an error sending your message") 
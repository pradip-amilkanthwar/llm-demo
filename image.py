from dotenv import load_dotenv

load_dotenv()

import streamlit as st
import google.generativeai as genai
import os
from PIL import Image

genai.configure(api_key=os.getenv("GOOGLE_API_KAY"))
model = genai.GenerativeModel("gemini-1.5-flash")


def get_model_response(input, image):
    if input != "":
        response = model.generate_content([image, input])
        return response.text
    else:
        response = model.generate_content(image)
        return response.text


st.set_page_config(page_title="Gemini pro image LLM Demo")
st.header("Large Image Model Application")
input = st.text_input("Input :", key="input")
uploaded_file = st.file_uploader("Choose an imahe ...", type=["jpg", "jpeg", "png"])
image = ""
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)


submit = st.button("Tell me about image")

if submit:
    response = get_model_response(input, image)
    st.subheader("response is ")
    st.write(response)

import pathlib
import streamlit as st
import os
from PIL import Image
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel("gemini-1.5-flash")


def compare_image(input, image1, image2):
    response = model.generate_content([input, image1, image2])
    return response.text


st.set_page_config(page_title="Gemini pro image comparison Demo")
st.header("Gemini Pro Image Comparison")
input = st.text_input("Input :", key="input")
image1 = st.file_uploader("Choose first Inage ...", type=["jpg", "jpeg", "png"])

first_image = ""
second_image = ""

if image1 is not None:
    first_image = Image.open(image1)
    st.image(first_image, caption="Uploaded Image", use_column_width=True)

image2 = st.file_uploader("Choose Second Image ...", type=["jpg", "jpeg", "png"])

if image2 is not None:
    second_image = Image.open(image2)
    st.image(second_image, caption="Uploaded Image", use_column_width=True)


submit = st.button("Tell me about image")

if submit:
    response = compare_image(input, first_image, second_image)
    st.subheader("response is ")
    st.write(response)

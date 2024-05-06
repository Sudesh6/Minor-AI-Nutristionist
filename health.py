### Health Management APP
from dotenv import load_dotenv

load_dotenv() ## load all the environment variables

import streamlit as st
import os
import google.generativeai as genai
from PIL import Image

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

## Function to load Google Gemini Pro Vision API And get response

def get_gemini_repsonse(input,image,prompt):
    model=genai.GenerativeModel('gemini-pro-vision')
    response=model.generate_content([input,image[0],prompt])
    return response.text
def input_image_setup(uploaded_file):
    # Check if a file has been uploaded
    if uploaded_file is not None:
        # Read the file into bytes
        bytes_data = uploaded_file.getvalue()

        image_parts = [
            {
                "mime_type": uploaded_file.type,  # Get the mime type of the uploaded file
                "data": bytes_data
            }
        ]
        return image_parts
    else:
        raise FileNotFoundError("No file uploaded")
    
##initialize our streamlit app

st.set_page_config(page_title="AI NUTRITIONIST")

st.header("AI NUTRITIONIST")
input=st.text_area("Input Prompt: ",key="input")

text=""
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
image=""   
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image.", use_column_width=True)

submit2=st.button("Diet")
submit1=st.button("Tell me the total calories")
submit3=st.button("food inspector")
input_prompt="""
You are an expert in nutritionist where you need to see the food items from the image
               and calculate the total calories, also provide the details of every food items with calories intake
               is below format

               1. Item 1 - no of calories
               2. Item 2 - no of calories
               ----
               ----


"""
input_prompt1="""
You are an expert in nutritionist where you need to see the food items from the image and give me the best healthy diet    
               and give me the best balanced diet
               is below format

               1. Item 1 - no of calories
               2. Item 2 - no of calories
               3. Item 3 - no of calories
               4. Item 4 - no of calories
               ----
               ----


"""
input_prompt2="""your are an expert in food inspection acts as my personal food inspector analyze the food image and tell me the whether the given image is a food item or not if it is a food item mainly highlight that the food is safe for health or not and also describe y the food is not healthy food 
"""

## If submit button is clicked

if submit1:
    image_data=input_image_setup(uploaded_file)
    response=get_gemini_repsonse(input_prompt,image_data,input)
    st.subheader("The Response is")
    st.write(response)


if submit2:
    image_data=input_image_setup(uploaded_file)
    response=get_gemini_repsonse(input_prompt1,image_data,input)
    st.subheader("The Response is")
    st.write(response)


if submit3:
    image_data=input_image_setup(uploaded_file)
    response=get_gemini_repsonse(input_prompt2,image_data,input)
    st.subheader("The Response is")
    st.write(response)


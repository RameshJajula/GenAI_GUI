# Import necessary libraries and modules
import streamlit as st
import os
import google.generativeai as genai
import PIL
# Path to your banner image (can be a local path or a URL)
banner_image = PIL.Image.open("C:\\Users\\rames\\OneDrive\\Desktop\\Logo\\Website.jpg")  # Replace with your image path

# Display the banner image
st.image(banner_image,width=None, use_column_width='always')

# Create a text input box in the sidebar
GOOGLE_API_KEY = st.sidebar.text_input("Enter your GOOGLE_API_KEY here")
genai.configure(api_key = GOOGLE_API_KEY)

# Create a list of activity options for selection
activity = ['TextWise', 'VisionWise']

# Use Streamlit's sidebar to allow users to select the model type
choice = st.sidebar.selectbox("Select Model type", activity)

# Import Markdown display for rendering generated content
from IPython.display import Markdown

# Initialize the text-based GenerativeModel with "gemini-pro"
model = genai.GenerativeModel("gemini-pro")

# Check the user's choice
if choice == 'TextWise':
    # Create a text area for users to enter a text prompt
    prompt = st.text_area("Enter prompt here:", height=200)
    
    # Check if the "Submit" button is clicked
    if st.button("Submit"):
        # Generate content based on the user's text prompt
        response = model.generate_content(prompt)
        
        # Display the generated content as Markdown
        st.markdown(response.text)

# Import Image display for showing images
from IPython.display import Image

# Initialize the image-based GenerativeModel with "gemini-pro-vision"
Model = genai.GenerativeModel('gemini-pro-vision')

# Check the user's choice
if choice == 'VisionWise':
    # Allow users to upload an image
    uploaded_file = st.file_uploader("Choose an image...", type=['jpg', 'jpeg', 'png'])

    # Display the uploaded image
    if uploaded_file is not None:
        image = PIL.Image.open(uploaded_file)
        st.image(image, caption='Uploaded Image.', use_column_width=True)
    
    # Create a text input for users to enter a prompt
    prompt = st.text_input('Enter prompt here:')
    
    # Check if the "Submit" button is clicked
    if st.button("Submit"):
        # Generate content based on the user's prompt and uploaded image
        response2 = Model.generate_content([prompt, image])
        
        # Display the generated content as Markdown
        st.markdown(response2.text)

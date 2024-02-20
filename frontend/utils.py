import os
import streamlit as st
import base64
from pdf2image import convert_from_bytes

def save_uploaded_file(uploaded_file, directory):
    if uploaded_file is not None:
        # Ensure the directory exists
        os.makedirs(directory, exist_ok=True)
        
        # Convert PDF pages to images
        images = convert_from_bytes(uploaded_file.getbuffer())
        
        # Save each page as an image
        for i, image in enumerate(images):
            image_path = os.path.join(directory, f"{uploaded_file.name}_page_{i+1}.png")
            image.save(image_path, "PNG")
        
    return None


def displayImage(image_path):
    # Check if the image exists
    if not os.path.exists(image_path):
        print(image_path)
        st.info("Give us your info so we can display it here.")
        return

    # Display the image
    st.image(image_path, width=700)
    
def display_images_from_folder(folder_path):
    images = os.listdir(folder_path)
    for image_name in images:
        image_path = os.path.join(folder_path, image_name)
        st.image(image_path, caption=image_name, use_column_width=True)


def displayPDF(uploaded_file):
    # Read file as bytes:
    bytes_data = uploaded_file.getvalue()
    # Convert to utf-8
    base64_pdf = base64.b64encode(bytes_data).decode("utf-8")
    # Embed PDF in HTML
    pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="700" height="300" type="application/pdf"></iframe>'
    # Display file
    st.markdown(pdf_display, unsafe_allow_html=True)
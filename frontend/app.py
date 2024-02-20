import os
import base64
import requests
import json
import sys
from pathlib import Path
# Add the parent directory to sys.path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from backend.utils import process_form
from PyPDF2 import PdfReader, PdfWriter
import streamlit as st
from utils import *
from backend.utils import process_form

def main():
    #image_path = 'final'
    st.header("💰 _Uncle Sam Tax_ 💰", divider="rainbow", help="Help?", anchor=False)
    # Split the window into two columns
    col1, col2 = st.columns(2)
    # Col1
    with col1:
        st.header("1️⃣: Hey, give me your info 🫵 ", anchor=False)
        tab1, tab2 = st.tabs(["Input", "Preview"])

        with tab1:
            st.subheader("How much money did you make? (W2 form)")
            st.caption('Your employer should have given it to you!')
            uploaded_file_w2 = st.file_uploader(
                "Choose Files",
                type="pdf",
                accept_multiple_files=True,
                help="Please submit your W-2",
                label_visibility="hidden",
            )
            st.subheader("Upload your last year's return (1040)")
            st.caption('Skip if you did not file taxes. Shame on you!')
            uploaded_file_1040 = st.file_uploader(
                "Choose Files",
                type="pdf",
                accept_multiple_files=True,
                help="Please submit 1040 from the previous year",
                label_visibility="hidden",
            )

            if st.button("Submit"):
                file_paths = []
                if uploaded_file_w2:
                    for file in uploaded_file_w2:
                        save_uploaded_file(file, "../data/w2_forms")
                        process_form("../prompts/w2_prompt.txt", "../data/w2_forms", "../data/info_w2.txt")
                    
                if uploaded_file_1040:
                    for file in uploaded_file_1040:
                        save_uploaded_file(file, "../data/past_1040_forms")
                        process_form("../prompts/1040_prompt.txt", "../data/past_1040_forms", "../data/info_1040.txt")


        with tab2:
            st.header("Preview of your uploaded forms")
            if uploaded_file_w2:
                for file in uploaded_file_w2:
                    displayPDF(file)

            if uploaded_file_1040:
                for file in uploaded_file_1040:
                    displayPDF(file)

    # Col2
    with col2:
        st.header("2️⃣: Now, file your taxes💰", anchor=False)
        tab3, tab4 = st.tabs(["Filled Form", "Download/E-File"])

        with tab3:
            st.subheader("Preview of your prepared tax form.")
            st.caption('Double check and dont mess up. Uncle sam will come after you')
            # displayImage(image_path)
            # display_images_from_folder(image_path)


        with tab4:
            st.header("Use us to E-File for you")
            st.button("Download to SnailMail it")
            st.button("E-File Now")


if __name__ == "__main__":
    main()
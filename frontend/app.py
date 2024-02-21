import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import json
from backend.utils import process_form, fill_tax_form
from PyPDF2 import PdfReader, PdfWriter
import streamlit as st
from utils import *

with open("../config.json", "r") as config_file:
    config = json.load(config_file)


st.set_page_config(page_title="", page_icon="💰", layout="wide")


def main():
    # image_path = 'final'
    st.header("💰 _Uncle Sam Tax_ 💰", divider="rainbow", help="Help?", anchor=False)
    # Split the window into two columns
    col1, col2 = st.columns(2)
    # Col1
    with col1:
        st.header("1️⃣: Hey, give me your info 🫵 ", anchor=False)
        tab1, tab2 = st.tabs(["Input", "Preview"])

        with tab1:
            st.subheader("How much money did you make? (W2 form)")
            st.caption("Your employer should have given it to you!")
            uploaded_file_w2 = st.file_uploader(
                "Choose Files",
                type="pdf",
                accept_multiple_files=True,
                help="Please submit your W-2",
                label_visibility="hidden",
            )
            st.subheader("Upload your last year's return (1040)")
            st.caption("Skip if you did not file taxes. Shame on you!")
            uploaded_file_1040 = st.file_uploader(
                "Choose Files",
                type="pdf",
                accept_multiple_files=True,
                help="Please submit 1040 from the previous year",
                label_visibility="hidden",
            )
            st.caption(
                "Tip: If you skip the uploads, we'll demo with handy Pre-Populated W-2 and 1040 Forms for you!"
            )

            if st.button(
                "Process Forms",
                help="If you skip the uploads, and we'll demo with handy Pre-Populated W-2 and 1040 Forms for you!",
            ):
                file_paths = []
                if uploaded_file_w2:
                    for file in uploaded_file_w2:
                        save_uploaded_file(file, config["W2_FORMS_DIR"])
                        process_form(
                            config["PROMPT_W2"],
                            config["W2_FORMS_DIR"],
                            config["INFO_DIR"],
                        )
                else:
                    process_form(
                        config["PROMPT_W2"], config["W2_FORMS_DIR"], config["INFO_DIR"]
                    )

                if uploaded_file_1040:
                    for file in uploaded_file_1040:
                        save_uploaded_file(file, config["PAST_1040_FORMS_DIR"])
                        process_form(
                            config["PROMPT_1040_PREV"],
                            config["PAST_1040_FORMS_DIR"],
                            config["INFO_DIR"],
                        )
                else:
                    process_form(
                        config["PROMPT_1040_PREV"],
                        config["PAST_1040_FORMS_DIR"],
                        config["INFO_DIR"],
                    )

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
            if st.button("Prepare Tax Form"):
                fill_tax_form(
                    config["PROMPT_F1040"],
                    config["F1040_FORM"],
                    config["FILLED_F1040_FORM"],
                )
                save_pdf_as_image(config["FILLED_F1040_FORM"])
                displayImage(config["FILLED_F1040_FORM_IMAGE"])
            st.caption("Double check and dont mess up. Uncle sam will come after you")

        with tab4:
            st.header("Use us to E-File for you")
            st.button("Download to SnailMail it")
            st.button("E-File Now")


if __name__ == "__main__":
    main()

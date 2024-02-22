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
import time


st.set_page_config(page_title="", page_icon="💰", layout="wide")


def process_data(progress_bar, delay, progress_increment, current_progress):
    """Simulate processing data, updating the progress bar accordingly."""
    time.sleep(delay)
    current_progress += progress_increment
    progress_bar.progress(current_progress)
    return current_progress


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
                progress_bar = st.progress(0)
                current_progress = 0

                current_progress = process_data(
                    progress_bar,
                    delay=1,
                    progress_increment=25,
                    current_progress=current_progress,
                )

                file_paths = []

                # W2 File Save
                if uploaded_file_w2:
                    current_progress = process_data(
                        progress_bar,
                        delay=1,
                        progress_increment=25,
                        current_progress=current_progress,
                    )
                    for file in uploaded_file_w2:
                        save_uploaded_file(file, config["W2_FORMS_DIR"])
                        process_form(
                            config["PROMPT_W2"],
                            config["W2_FORMS_DIR"],
                            config["INFO_DIR"],
                        )

                else:
                    current_progress = process_data(
                        progress_bar,
                        delay=1,
                        progress_increment=25,
                        current_progress=current_progress,
                    )
                    process_form(
                        config["PROMPT_W2"], config["W2_FORMS_DIR"], config["INFO_DIR"]
                    )

                # 1040 File Save
                if uploaded_file_1040:
                    current_progress = process_data(
                        progress_bar,
                        delay=1,
                        progress_increment=25,
                        current_progress=current_progress,
                    )

                    for file in uploaded_file_1040:
                        save_uploaded_file(file, config["PAST_1040_FORMS_DIR"])
                        process_form(
                            config["PROMPT_1040_PREV"],
                            config["PAST_1040_FORMS_DIR"],
                            config["INFO_DIR"],
                        )
                else:
                    current_progress = process_data(
                        progress_bar,
                        delay=1,
                        progress_increment=25,
                        current_progress=current_progress,
                    )
                    process_form(
                        config["PROMPT_1040_PREV"],
                        config["PAST_1040_FORMS_DIR"],
                        config["INFO_DIR"],
                    )
                process_data(
                    progress_bar,
                    delay=1,
                    progress_increment=25,
                    current_progress=current_progress,
                )
                progress_bar.empty()
                st.success("All processes completed!")

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
                progress_bar = st.progress(0)
                current_progress = 0

                current_progress = process_data(
                    progress_bar,
                    delay=1,
                    progress_increment=33,
                    current_progress=current_progress,
                )

                fill_tax_form(
                    config["PROMPT_F1040"],
                    config["F1040_FORM"],
                    config["FILLED_F1040_FORM"],
                )

                current_progress = process_data(
                    progress_bar,
                    delay=1,
                    progress_increment=33,
                    current_progress=current_progress,
                )

                save_pdf_as_image(config["FILLED_F1040_FORM"])
                displayImage(config["FILLED_F1040_FORM_IMAGE"])

                process_data(
                    progress_bar,
                    delay=1,
                    progress_increment=34,
                    current_progress=current_progress,
                )

                progress_bar.empty()

                st.success("All processes completed!")

            st.caption("Double check and dont mess up. Uncle sam will come after you")

        with tab4:
            st.header("Use us to E-File for you")
            st.button("Download to SnailMail it")
            st.button("E-File Now")


if __name__ == "__main__":
    main()

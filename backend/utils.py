import os
import json
from PyPDF2 import PdfReader, PdfWriter
from .models import VisionModel, TextModel

def process_form(prompt_path, img_paths, out_path):
    try:
        vision_model = VisionModel()
        with open(prompt_path, "r", encoding="utf-8") as f:
            prompt = f.read()
        response = vision_model.complete(prompt, img_paths)
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(response)
    except Exception as e:
        print(f"An error occurred: {e}")


def fill_tax_form(prompt_path, input_pdf_path, output_pdf_path):
    # Directory containing the text files
    info_path = "data/info"
    
    # Initialize an empty string to hold the combined text
    info = ""
    
    # Loop through each file in the specified directory
    for filename in os.listdir(info_path):
        # Check if the file is a .txt file
        if filename.endswith(".txt"):
            # Construct full file path
            file_path = os.path.join(info_path, filename)
            # Open and read the text file, then append its content to `info`
            with open(file_path, "r", encoding="utf-8") as f:
                info += f.read() + "\n"  # Add a newline to separate contents of different files

    # Read the prompt file
    with open(prompt_path, "r", encoding="utf-8") as f:
        context = f.read()
    text_model = TextModel()
    str_response = text_model.complete(info + context)
    json_response = json.loads(str_response)
    fill_pdf_form(json_response, input_pdf_path, output_pdf_path)

def fill_pdf_form(form_data, input_pdf_path, output_pdf_path):

  reader = PdfReader(input_pdf_path)
  writer = PdfWriter()

  # Copy all pages from the reader to the writer
  for page in reader.pages:
    writer.add_page(page)

  # Attempt to directly modify the '/V' value (not effective in this context)
  # Instead, prepare the form fields data based on the JSON file
  fields = {field: form_data.get(field, '') for field in reader.get_form_text_fields()}

  # Update the fields in the writer object for each page
  for page in writer.pages:
    writer.update_page_form_field_values(page, fields)

  # Write the output PDF file
  with open(output_pdf_path, 'wb') as output_pdf:
    writer.write(output_pdf)
  print(f"PDF form filled and saved to '{output_pdf_path}'.")





# 1040-GPT

## Let GPT-4 Fill Your 1040s

Welcome to our innovative application designed to simplify the tax filing process using the power of GPT-4. With `1040-GPT`, we aim to revolutionize how individuals and businesses complete their tax forms, making it faster, more accurate, and less stressful.

Our application leverages the advanced natural language processing capabilities of GPT-4 to understand and process W2 and 1040 tax forms. Whether you're struggling with tax preparation or just looking for a way to streamline the process, our tool is here to assist. By automating the form-filling process, we minimize errors and maximize efficiency, allowing you to focus on what matters most.

Follow the setup and usage instructions below to get started and experience a hassle-free tax season.

## Getting Started

Follow these steps to set up your environment and run the application.

### Step 1: Install Dependencies

Before running the application, you need to install the required Python packages. Open a terminal and navigate to the root directory of this project. Then run the following command:

``` bash
pip install -r requirements.txt
```

This command reads the `requirements.txt` file and installs the Python packages listed there.

### Step 2: Set Up Environment Variables

You need to configure the required environment variables for the application. Create a `.env` file in the root directory and add your `OPEN_AI_API_KEY` and `PORTKEY_API_KEY` as follows:

``` bash
OPEN_AI_API_KEY=<your_open_ai_api_key>
PORTKEY_API_KEY=<your_portkey_api_key>
```

Replace `<your_open_ai_api_key>` and `<your_portkey_api_key>` with your actual API keys.

### Step 3: Run the Application

To start the application, navigate to the `frontend/` directory and run the following command:

`streamlit run app.py`

This command launches the Streamlit application in your default web browser.

## Using the Application

Once the application is running, follow these steps to process and preview your tax forms:

1. **Upload Forms:** In the web interface that opens, upload your W2 and 1040 forms by clicking on the respective upload buttons.

2. **Process Forms:** After uploading the forms, click on the "Process Forms" button to start the processing. The application will analyze the uploaded documents.

3. **Preview Tax Forms:** Upon successful processing, click on the "Prepare Tax Forms" button to get a preview of the filled form. You can review the information extracted and filled into the form.

## Notes

- Ensure your `.env` file is never shared or committed to a public repository. Include it in your `.gitignore` file to prevent accidental exposure of your API keys.

- If you encounter any issues or need further assistance, please refer to the application documentation or contact support.

Thank you for using our application!

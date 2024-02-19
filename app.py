import os
import base64
import requests
import json
from PyPDF2 import PdfReader, PdfWriter
import streamlit as st
from dotenv import load_dotenv

load_dotenv()

st.header("PDF to Text")


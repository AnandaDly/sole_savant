import os
import streamlit as st
from supabase import create_client
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize Supabase client
@st.cache_resource
def init_connection():
    URL = os.getenv('SUPABASE_URL')
    KEY = os.getenv('SUPABASE_KEY')
    return create_client(URL, KEY)

def supabase():
    return init_connection()
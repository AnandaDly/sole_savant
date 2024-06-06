import streamlit as st
import hashlib
import importlib.util
import sys
import os

# get absolute path from connection.py
connection_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'config', 'connection.py'))

spec = importlib.util.spec_from_file_location("connection", connection_path)
connection = importlib.util.module_from_spec(spec)
sys.modules["connection"] = connection
spec.loader.exec_module(connection)

supabase = connection.init_connection()

# Function to hash passwords 
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Function to verify user credentials with Supabase
def verify_user(username, password):
    hashed_password = hash_password(password)
    try:
        result = supabase.table('users').select('*').eq('username', username).eq('password', hashed_password).execute()
        if result.data:
            return True
        else:
            return False
    except Exception as e:
        st.error(f"Error: {str(e)}")
        return False

def login():
#def app():
    st.title("Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    
    if st.button("Login"):
        if verify_user(username, password):
            st.session_state['authenticated'] = True
            st.session_state['username'] = username 
            st.rerun()
        else:
            st.error("Invalid username or password")

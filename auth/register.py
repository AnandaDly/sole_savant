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

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Function to check for duplicate username or email
def check_duplicate_username_or_email(username, email):
    try:
        existing_users = supabase.table('users').select("*").or_(f"username.eq.{username},email.eq.{email}").execute()
        return existing_users.data
    except Exception as e:
        return {"error": str(e)}

# Function to register a new user
def register_user(username, email, password):
    hashed_password = hash_password(password)
    data = {
        "username": username,
        "email": email,
        "password": hashed_password
    }
    try:
        result = supabase.table('users').insert(data).execute()
        return result   
    except Exception as e:
        return {"error": str(e)}

def register():
    st.title("Register")
 
    with st.form(key='registration_form'):
        username = st.text_input("Username")
        email = st.text_input("Email")
        password = st.text_input("Password", type="password")
        confirm_password = st.text_input("Confirm Password", type="password")
        
        submit_button = st.form_submit_button(label='Register')
    
    if submit_button:
        if not username or not email or not password or not confirm_password:
            st.error("All fields are required")
        elif password != confirm_password:
            st.error("Passwords do not match")
        else:
            duplicates = check_duplicate_username_or_email(username, email)
            if isinstance(duplicates, dict) and 'error' in duplicates:
                st.error(f"Error checking for duplicates: {duplicates['error']}")
            elif duplicates and len(duplicates) > 0:
                st.error("Username or Email already exists")
            else:
                result = register_user(username, email, password)
                if isinstance(result, dict) and 'error' in result:
                    st.error(f"Registration failed: {result['error']}")
                else:
                    st.success("Registration successful!")
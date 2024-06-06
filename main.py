import streamlit as st
from auth import login, register
from func import apps, homepage


def app():
    st.sidebar.title("Navigation")
    menu = st.sidebar.selectbox("Select a Menu", ('Read Data', 'Classification', 'Sentiment Analysis'))

    if menu == 'Read Data':
        apps.read_data()
    elif menu == 'Classification':
        apps.classification()
    elif menu == 'Sentiment Analysis':
        apps.sentiment_analysis()

# Entry point of the application
if __name__ == '__main__':
    if 'authenticated' not in st.session_state:
        st.session_state['authenticated'] = False
    if st.session_state['authenticated']:
        st.sidebar.write(f"Welcome, {st.session_state['username']}!")   
        st.sidebar.button("Logout", on_click=lambda: st.session_state.update({'authenticated': False}))
        app()
    else:
        page = st.sidebar.selectbox("Select a Page", ["Homepage", "Login", "Register"])
        if page == "Homepage":
            homepage.homepage()
        elif page == "Login":
            login.login()
        elif page == "Register":
            register.register()

import base64
import streamlit as st

def add_bg_from_local(image_file):
    with open(image_file, "rb") as file:
        encoded_string = base64.b64encode(file.read())
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url(data:image/png;base64,{encoded_string.decode()});
            background-size: cover;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

def get_custom_css():
    return """
    <style>
    .flowchart-container {
        background-color: rgba(30, 30, 45, 0.9);
        border-radius: 10px;
        padding: 20px;
        margin: 20px 0;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    
    .flowchart-container img {
        background-color: #1e1e2d;
        border-radius: 8px;
        padding: 15px;
    }
    
    .stTextArea textarea {
        background-color: rgba(34, 34, 51, 0.7);
        color: #fff;
        font-family: 'Courier New', monospace;
        font-size: 14px;
        border-radius: 8px;
        border: 1px solid #444;
        padding: 10px;
    }
    
    .stButton>button {
        background-color: #5a67d8;
        color: white;
        border: none;
        padding: 10px 20px;
        font-size: 16px;
        border-radius: 8px;
        cursor: pointer;
    }
    
    .stButton>button:hover {
        background-color: #4c51bf;
    }
    
    .stMarkdown h1, .stMarkdown p {
        margin-top: 0;
    }
    
    .stMarkdown h1 {
        font-size: 3em;
        color: #fff;
        text-align: center;
        margin-bottom: 30px;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.5);
    }
    
    .stMarkdown p {
        text-align: center;
        color: #d1d5db;
        font-size: 1.2em;
        margin-bottom: 40px;
        text-shadow: 1px 1px 2px rgba(0,0,0,0.5);
    }
    
    .footer {
        position: fixed;
        bottom: 0;
        left: 0;
        right: 0;
        background-color: rgba(30, 0, 60, 0.9);
        padding: 10px 0;
        text-align: center;
        color: #a0aec0;
        font-size: 14px;
    }
    </style>
    """
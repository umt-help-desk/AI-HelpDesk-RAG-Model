import streamlit as st


def apply_styles():
    st.markdown("""
        <style>
        body {
            font-family: 'Arial', sans-serif;
            background-color: #1e1e1e;
            color: #ececec;
            padding: 20px;
        }

        h1 {
            text-align: center;
            font-size: 2.8rem;
            font-weight: bold;
            color: #00bfae;
            margin-bottom: 20px;
        }

        .chat-container {
            background-color: #2a2a2a;
            border-radius: 15px;
            padding: 20px;
            margin-bottom: 20px;
            box-shadow: 0 4px 10px rgba(0, 0, 0, 0.2);
        }

        .chat-user {
            background-color: #007bff;
            color: white;
            padding: 12px 18px;
            border-radius: 20px;
            margin-bottom: 10px;
            font-size: 1.1rem;
            font-weight: bold;
        }

        .chat-bot {
            background-color: #ff5f61;
            color: white;
            padding: 12px 18px;
            border-radius: 20px;
            margin-bottom: 10px;
            font-size: 1.1rem;
            font-weight: normal;
        }

        .stTextInput input {
            background-color: #2d2d2d;
            color: #ececec;
            padding: 12px;
            border-radius: 8px;
            border: 2px solid #444;
            font-size: 1.1rem;
            width: 100%;
        }

        .stTextInput input:focus {
            border-color: #00bfae;
            background-color: #252525;
            outline: none;
        }

        .stButton button {
            background-color: #00bfae;
            color: white;
            font-size: 1.1rem;
            font-weight: bold;
            padding: 10px 30px;
            border-radius: 8px;
            transition: 0.3s ease-in-out;
        }

        .stButton button:hover {
            background-color: #008a7d;
            transform: scale(1.05);
        }

        .stTextArea textarea {
            background-color: #2d2d2d;
            color: white;
            border: 2px solid #444;
            padding: 12px;
            font-size: 1.1rem;
            border-radius: 8px;
            width: 100%;
        }

        .stTextArea textarea:focus {
            border-color: #00bfae;
            background-color: #252525;
            outline: none;
        }

        .stMarkdown {
            background-color: #2a2a2a;
            padding: 12px;
            border-radius: 10px;
            margin-top: 10px;
            box-shadow: 0px 2px 5px rgba(0, 0, 0, 0.1);
        }
        
        /* Adjust alignment for messages */
        .stMarkdown h3 {
            font-size: 1.3rem;
            color: #00bfae;
        }

        </style>
    """, unsafe_allow_html=True)

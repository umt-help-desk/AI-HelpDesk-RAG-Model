import streamlit as st
from transformers import pipeline
from design import apply_styles

# Streamlit setup
st.set_page_config(page_title="AI Help Desk Chatbot", layout="wide")
st.title("🤖 AI Help Desk Chatbot")
st.write("Welcome to the AI Help Desk Chatbot! Ask me anything about UMT-PRS, and I'll provide accurate and helpful answers.")

# Apply UI styles
apply_styles()

# Load models dynamically (avoid storing them in repo)
@st.cache_resource  # Ensures the model is loaded only once per session
def load_models():
    summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
    generator = pipeline("text-generation", model="MBZUAI/LaMini-GPT-774M")  # Using a smaller model for efficiency
    return summarizer, generator

summarizer, generator = load_models()

# Function to generate response
def generate_response(user_query):
    summary = summarizer(user_query, max_length=100, min_length=30, do_sample=False)[0]['summary_text']
    response = generator(summary, max_length=150)[0]['generated_text']
    return response

# Process user queries
def process_query(query):
    if not query.strip():
        st.warning("⚠️ Please enter a valid question.")
        return

    with st.spinner("🔎 Searching for the best answer..."):
        try:
            answer = generate_response(query)
            st.subheader("📌 Your Query:")
            st.info(query)
            st.subheader("📝 Answer:")
            st.success(answer)
        except Exception as e:
            st.error(f"❌ An unexpected error occurred: {str(e)}")
            st.warning("Try rewording your question or contact support if the issue persists.")

# Input field with form submission
with st.form(key="user_input_form", clear_on_submit=False):
    user_query = st.text_input("💬 Ask Your Question:", placeholder="Type your question here...")
    submit_button = st.form_submit_button(label="🚀 Send")

    if submit_button and user_query:
        process_query(user_query)

import streamlit as st
from design import apply_styles
from utils import get_final_answer  # ✅ Use the new function

# Streamlit setup
st.set_page_config(page_title="AI Help Desk Chatbot", layout="wide")
st.title("🤖 AI Help Desk Chatbot")
st.write("Welcome to the AI Help Desk Chatbot! Ask me anything about UMT-PRS, and I'll provide accurate and helpful answers.")

# Apply design styles
apply_styles()


# Function to process user queries
def process_query(query):
    if not query.strip():
        st.warning("⚠️ Please enter a valid question.")
        return

    with st.spinner("🔎 Searching for the best answer..."):
        try:
            # ✅ Call the new pipeline function
            results = get_final_answer(query)

            # Display results
            st.subheader("📌 Your Query:")
            st.info(query)
            st.subheader("📝 Answer:")
            st.success(results["answer"])
            with st.expander("📂 Reference Context (Click to View)"):
                st.write(results["reference_context"])

        except Exception as e:
            st.error(f"❌ An unexpected error occurred: {str(e)}")
            st.warning(
                "Try rewording your question or contact support if the issue persists.")


# Input field with form submission
with st.form(key="user_input_form", clear_on_submit=False):
    user_query = st.text_input(
        "💬 Ask Your Question:", placeholder="Type your question here...")
    submit_button = st.form_submit_button(label="🚀 Send")

    if submit_button and user_query:
        process_query(user_query)

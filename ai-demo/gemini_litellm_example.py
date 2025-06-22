import streamlit as st
import litellm
import os
from dotenv import load_dotenv

# Load .env
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

# UI
st.set_page_config(page_title="Gemini Chatbot 💬", layout="centered")
st.title("🤖 Gemini + LiteLLM Chat App")
st.markdown("Ask anything, and get a response powered by **Gemini via LiteLLM**!")

# User input
prompt = st.text_input("💬 Enter your message:")

# Response
if st.button("Ask Gemini") and prompt:
    with st.spinner("Thinking..."):
        try:
            response = litellm.completion(
                model="gemini/gemini-1.5-flash",
                messages=[{"role": "user", "content": prompt}],
                api_key=api_key
            )
            reply = response['choices'][0]['message']['content']
            st.success("✅ Gemini says:")
            st.write(reply)
        except Exception as e:
            st.error(f"❌ Error: {str(e)}")

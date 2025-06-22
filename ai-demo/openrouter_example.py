import streamlit as st
import litellm
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
api_key = os.getenv("OPENROUTER_API_KEY")

st.set_page_config(page_title="OpenRouter Chat", page_icon="🤖")

st.title("🧠 OpenRouter LLM Chat")
st.write("Ask anything from OpenRouter using Mistral model!")

# User input
user_input = st.text_input("Enter your question:")

if user_input:
    try:
        response = litellm.completion(
            model="mistralai/mistral-7b-instruct",
            messages=[{"role": "user", "content": user_input}],
            api_key=api_key,
            api_base="https://openrouter.ai/api/v1",
            custom_llm_provider="openrouter"
        )
        st.subheader("💬 Response:")
        st.write(response['choices'][0]['message']['content'])

    except Exception as e:
        st.error(f"❌ Error: {e}")

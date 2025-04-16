import streamlit as st
import google.generativeai as genai
import re 

# Setup Gemini API
api_key = st.secrets["google"]["gemini_api_key"]
genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-1.5-pro")

# Helper function to format poem with line breaks
def format_poem(text):
    lines = re.split(r'(?<=[.!?])\s+', text)
    return "\n".join(line.strip() for line in lines if line.strip())

# Function to generate poetry based on mood, theme, and custom words
def generate_poetry(mood, theme, custom_words):
    prompt = f"Write a poem based on the mood: {mood}, theme: {theme}, and include the words: {', '.join(custom_words)}. Use poetic lines, not paragraphs."

    response = model.generate_content(contents=prompt)

    if hasattr(response, "text"):
        raw_poem = response.text.strip()
        formatted_poem = format_poem(raw_poem)
        return formatted_poem
    return "Error generating poem."

# Add custom styling
st.markdown("""
    <style>
        body {
            background-color: #f0f0f0;
            color: #333;
        }
        .sidebar .sidebar-content {
            background-color: #ffe600;
        }
        .stButton>button {
            background-color: #00aaff;
            color: white;
            font-weight: bold;
            padding: 10px 15px;
        }
        h1 {
            color: #00aaff;
        }
        h2 {
            color: #ff6600;
        }
        .stTextInput, .stTextArea {
            margin-top: 10px;
        }
    </style>
""", unsafe_allow_html=True)

# Header and description
st.title("Poetry Generator Bot")
st.write("Generate beautiful poems based on your mood, theme, and custom words.")

# Sidebar for customization options
st.sidebar.header("Customize Your Poem")
mood = st.sidebar.selectbox("Select Mood", ["Happy", "Sad", "Romantic", "Mystical", "Melancholy"])
theme = st.sidebar.selectbox("Select Theme", ["Nature", "Love", "Life", "Dreams", "Adventure"])
custom_words_input = st.sidebar.text_area("Provide Custom Words (optional)", "")
custom_words = [word.strip() for word in custom_words_input.split(',')] if custom_words_input else []

# Placeholder for poem
poem = ""

# Button to generate poetry
if st.sidebar.button("Generate Poem"):
    with st.spinner("Generating your poem..."):
        poem = generate_poetry(mood, theme, custom_words)

    # Display generated poem
    st.subheader("Your Generated Poem")
    st.markdown(f"```markdown\n{poem}\n```", unsafe_allow_html=True)

    # Add download button
    st.download_button(" Download Poem", poem, file_name="generated_poem.txt")

# Footer
st.markdown("""
    <footer style="text-align: center; margin-top: 40px; font-size: 12px; color: #666;">
        <p>Poetry Generator Bot | Built with Streamlit & Gemini API</p>
    </footer>
""", unsafe_allow_html=True)

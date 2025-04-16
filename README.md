

A simple Streamlit web app that generates beautiful poems based on your mood, theme, and custom words using Google's Gemini 1.5 Pro API.

##  Features
- Choose your **mood** 
- Pick a **theme** 
- Add **custom words** to personalize the poem
- Get the result in a proper poetic format
- Copy or download the generated poem

## 🛠 Tech Stack
- [Streamlit](https://streamlit.io/)
- [Gemini API (Google Generative AI)](https://ai.google.dev/)
- Python 3.9+

## 🚀 Setup Instructions

1. **Clone the repository**  
   ```bash
   git clone https://github.com/your-username/Poem-Generator.git
   cd Poem-Generator
2. **Install dependencies**
   pip install -r requirements.txt
3. **Set your Gemini API key**
   genai.configure(api_key="your_api_key_here")
4. **Run the Streamlit app**
   streamlit run app.py
   
📝 License
This project is licensed under the MIT License.

💡 Future Ideas
Add support for saving poem history
Share poems via email or social media
Add more moods/themes and style formats

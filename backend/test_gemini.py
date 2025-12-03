import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
print(f"API Key loaded: {api_key[:20]}...")  # Don't print full key
try:
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-2.0-flash')
    response = model.generate_content("Say hello")
    print("✅ API Key works!")
except Exception as e:
    print(f"❌ Error: {e}")
from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv(dotenv_path="config/config.env")

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
api_key = os.getenv("OPENAI_API_KEY")

if api_key:
    print(f"✅ OpenAI API Key Loaded: {api_key[:6]}...{api_key[-4:]}")
else:
    print("❌ OpenAI API Key not found!")

client = OpenAI(api_key=api_key)

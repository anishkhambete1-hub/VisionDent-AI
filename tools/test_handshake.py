import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types

def test_gemini_connection():
    """
    Minimal handshake script to verify the Gemini API connection.
    """
    # 1. Load environment variables
    load_dotenv()
    api_key = os.getenv("GEMINI_API_KEY")
    
    if not api_key or api_key == "your_google_gemini_api_key_here":
        print("❌ Error: GEMINI_API_KEY not found or not set in .env file.")
        print("Please update the .env file with your actual API key.")
        sys.exit(1)

    print("✅ API Key found.")

    try:
        # 2. Initialize the client
        print("Initializing Gemini Client...")
        client = genai.Client(api_key=api_key)

        # 3. Simple text generation test
        print("Sending ping to Gemini 1.5 Flash...")
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents='Respond with only the word "PONG".'
        )

        
        if response.text and "PONG" in response.text.upper():
            print(f"✅ Handshake successful! Received: {response.text.strip()}")
            return True
        else:
             print(f"⚠️ Handshake returned unexpected result: {response.text}")
             return False

    except Exception as e:
        print(f"❌ Connection failed: {e}")
        sys.exit(1)

if __name__ == "__main__":
    print("--- Phase 2: Link Handshake Test ---")
    test_gemini_connection()

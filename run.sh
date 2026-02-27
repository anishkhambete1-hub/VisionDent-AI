#!/bin/bash
# VisiDent-AI Trigger Script

echo "🦷 Starting VisiDent-AI Clinical Analyzer..."

# 1. Check if the virtual environment exists
if [ ! -d ".venv" ]; then
    echo "❌ Error: Virtual environment '.venv' not found."
    echo "Please ensure you have run the setup commands to install dependencies."
    exit 1
fi

# 2. Activate the environment
source .venv/bin/activate

# 3. Check for the .env file with API key
if [ ! -f ".env" ]; then
    echo "⚠️ Warning: '.env' file not found. Ensure GOOGLE_API_KEY is set in your environment variables!"
fi

# 4. Trigger the Streamlit User Interface
echo "🚀 Launching Streamlit UI..."
streamlit run app.py

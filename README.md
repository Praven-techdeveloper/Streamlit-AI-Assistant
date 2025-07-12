# Streamlit-AI-Assistant

Local AI Assistant with Ollama

A Streamlit-based chat application that runs entirely on your local machine using Ollama. Interact with powerful open-source large language models (LLMs) without internet connection, API keys, or costs. Your conversations stay 100% private on your device.

Features
100% Local & Private: No data leaves your computer

No API Keys Required: Completely free to use

Multiple Models: Supports llama3, mistral, phi3, gemma and more

Model Management: Install new models directly from the app

Adjustable Parameters: Control creativity and response length

Streaming Responses: Real-time token streaming

Offline Capable: Works without internet after setup

Cross-Platform: Runs on Windows, macOS, and Linux


Quick Start
Prerequisites
Python 3.8+

Ollama installed

4GB+ RAM (8GB+ recommended for larger models)

Installation
bash
# Create virtual environment (recommended)
python -m venv ollama-env
source ollama-env/bin/activate  # Linux/Mac
ollama-env\Scripts\activate    # Windows

# Install dependencies
pip install streamlit ollama


Run the App
bash
streamlit run app.py


Recommended Models
Model	Parameters	Best For	RAM Needed	Speed
llama3	8B	General purpose	8GB+	⚡⚡⚡
mistral	7B	Reasoning tasks	8GB+	⚡⚡
phi3	3.8B	Fast responses	4GB+	⚡⚡⚡⚡
gemma	2B	Basic tasks	4GB+	⚡⚡⚡⚡⚡

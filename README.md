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
Usage Guide
1.Install Models:

Use the sidebar to install models like llama3

Or via terminal: ollama pull llama3


2.Select Model:

Choose from installed models in the dropdown

Adjust temperature (creativity) and max length

3.Start Chatting:

Type your question in the chat box

Responses stream in real-time

Use "Clear Conversation" to reset chat

4.Install New Models:

Type model name in "Install New Models" section

Click "Install Model" button

Popular options: mistral, phi3, gemma

Troubleshooting
Ollama not detected:

Ensure Ollama is running in background

Check with ollama list in terminal

Restart computer after installation

Slow first response:

Models load into memory on first use

Subsequent responses are faster

Try smaller models like phi3 or gemma

Out of memory errors:

Close other applications

Use smaller models

Reduce max response length

Add more RAM if possible

Model installation issues:

Check internet connection

Verify model name is correct

Ensure sufficient disk space (models are 2-5GB each)

Performance Tips
Start with smaller models like phi3 or gemma if you have limited RAM

Close memory-intensive applications before using larger models

Use shorter responses by reducing max length

Be patient on first run - models need to load into memory

Consider hardware upgrades if using larger models frequently

Development
Requirements
Python 3.8+

Streamlit

Ollama Python package

File Structure
text
local-ai-assistant/
├── app.py              # Main application code
├── requirements.txt    # Python dependencies
└── README.md           # This documentation
Running Tests
bash
# No formal tests yet - manual testing via UI
License
This project is licensed under the MIT License 

Acknowledgments
Ollama for the local model infrastructure

Streamlit for the web app framework

Meta, Mistral AI, Microsoft, and Google for the open-source models

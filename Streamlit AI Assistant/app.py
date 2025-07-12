import streamlit as st
import ollama
import time
import subprocess

st.set_page_config(
    page_title="Enhanced AI Assistant",
    page_icon="🤖",
    layout="wide"
)
if 'generated' not in st.session_state:
    st.session_state.generated = []
    
if 'past' not in st.session_state:
    st.session_state.past = []
    
if 'available_models' not in st.session_state:
    st.session_state.available_models = ["llama3", "mistral", "phi3"]

# Function to get installed Ollama models
def get_installed_models():
    try:
        models = ollama.list()['models']
        return [model['name'] for model in models]
    except:
        return st.session_state.available_models

 
with st.sidebar:
    st.title("⚙️ Local AI Configuration")
    available_models = get_installed_models()
    
    # Model selection
    selected_model = st.selectbox(
        "Select Model:",
        available_models,
        index=0
    )
    
    st.markdown("---")
    st.subheader("Model Parameters")
    temperature = st.slider("Creativity:", 0.0, 1.0, 0.7)
    max_length = st.slider("Response Length:", 10, 1000, 512)
    
    st.markdown("---")
    st.subheader("Install New Models")
    new_model = st.text_input("Model name to install:", "llama3")
    if st.button("Install Model"):
        with st.spinner(f"Installing {new_model}..."):
            try:
                # Run ollama pull in a subprocess
                process = subprocess.Popen(
                    ["ollama", "pull", new_model],
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    text=True
                )
                
                 
                output_container = st.empty()
                while True:
                    output = process.stdout.readline()
                    if output == '' and process.poll() is not None:
                        break
                    if output:
                        output_container.write(output.strip())
                
                st.success(f"Model {new_model} installed successfully!")
                 
                st.session_state.available_models = get_installed_models()
                st.experimental_rerun()
            except Exception as e:
                st.error(f"Error installing model: {str(e)}")
    
    st.info("Popular models: `llama3`, `mistral`, `phi3`, `gemma`")
    
    st.markdown("---")
    st.caption("💡 All models run locally with no internet connection needed")
    st.caption("⚠️ First response may be slow as models load into memory")

# Main app interface
st.title("🤖 Enhanced AI Assistant")
st.subheader("100% Free, Private & Offline")

# Display model info
current_model = selected_model.split(":")[0]   
st.info(f"**Current Model:** `{current_model}` | **Creativity:** {temperature} | **Max Length:** {max_length}")

# Function for generating responses
def generate_response(prompt):
    try:
        
        response = ollama.chat(
            model=selected_model,
            messages=[{'role': 'user', 'content': prompt}],
            stream=True,
            options={
                'temperature': temperature,
                'num_predict': max_length
            }
        )
        
        
        full_response = []
        for chunk in response:
            if chunk['message']['content']:
                text_chunk = chunk['message']['content']
                full_response.append(text_chunk)
                yield text_chunk
                
        # Save complete response
        st.session_state.generated.append(''.join(full_response))
        
    except Exception as e:
        yield f"⚠️ Error: {str(e)}"

# Display conversation history
for i, (user_msg, ai_msg) in enumerate(zip(st.session_state.past, st.session_state.generated)):
    with st.chat_message("user"):
        st.write(user_msg)
    with st.chat_message("assistant"):
        st.write(ai_msg)

# Chat input
if prompt := st.chat_input("Ask anything..."):
    # Add user message to history
    st.session_state.past.append(prompt)
    
    # Display user message
    with st.chat_message("user"):
        st.write(prompt)
    
    # Generate and display assistant response
    with st.chat_message("assistant"):
        response = st.write_stream(generate_response(prompt))

# Add clear conversation button
if st.button("Clear Conversation"):
    st.session_state.generated = []
    st.session_state.past = []
    st.experimental_rerun()

# Model information section
st.markdown("---")
st.subheader("About Your Local AI")

# Recommended models
st.info("""
**Recommended Models:**
- `llama3`: Meta's latest model (8B parameters) - great all-purpose assistant
- `mistral`: Excellent reasoning (7B parameters) - good for complex questions
- `phi3`: Microsoft's efficient model (3.8B parameters) - fast responses
- `gemma`: Google's lightweight model (2B parameters) - good for basic tasks
""")

# Performance tips
with st.expander("Performance Tips"):
    st.markdown("""
    **For Best Performance:**
    1. **Install models first** using the sidebar installer
    2. **Close other applications** to free up RAM
    3. **Start with smaller models** like `phi3` or `gemma`
    4. **Use shorter responses** by reducing max length
    5. **Be patient** on first run - models need to load
    
    **Hardware Requirements:**
    - 8GB RAM: Works with smaller models (phi3, gemma)
    - 16GB RAM: Good for medium models (mistral)
    - 32GB RAM: Best for larger models (llama3)
    """)

# Add model cards
st.markdown("---")
st.subheader("Model Comparison")

model_data = [
    {"Model": "llama3", "Parameters": "8B", "Best For": "General purpose", "RAM": "8GB+", "Speed": "⚡⚡⚡"},
    {"Model": "mistral", "Parameters": "7B", "Best For": "Reasoning tasks", "RAM": "8GB+", "Speed": "⚡⚡"},
    {"Model": "phi3", "Parameters": "3.8B", "Best For": "Fast responses", "RAM": "4GB+", "Speed": "⚡⚡⚡⚡"},
    {"Model": "gemma", "Parameters": "2B", "Best For": "Basic tasks", "RAM": "4GB+", "Speed": "⚡⚡⚡⚡⚡"},
]

 
cols = st.columns(len(model_data))
for i, model in enumerate(model_data):
    with cols[i]:
        st.subheader(model["Model"])
        st.caption(f"{model['Parameters']} parameters")
        st.write(f"**Best for:** {model['Best For']}")
        st.write(f"**RAM needed:** {model['RAM']}")
        st.write(f"**Speed:** {model['Speed']}")
        if st.button(f"Install {model['Model']}", key=f"install_{model['Model']}"):
            st.session_state.new_model = model['Model']
            st.experimental_rerun()

st.markdown("---")
st.caption("Local AI Assistant v1.0 | Runs 100% offline after setup | No tracking | No costs")

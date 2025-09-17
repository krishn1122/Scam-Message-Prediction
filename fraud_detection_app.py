"""
Streamlit app for fraud detection using Llama-3.2-1B-Instruct model.
"""

import streamlit as st
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

# Set page config
st.set_page_config(
    page_title="Scam Message Predictor",
    page_icon="🚨",
    layout="wide"
)

# Custom CSS for theming
st.markdown("""
<style>
    .stApp {
        background-color: #f0f2f6;
    }
    .header {
        background-color: #ff4b4b;
        padding: 20px;
        border-radius: 10px;
        text-align: center;
        color: white;
        margin-bottom: 30px;
    }
    .result-card {
        background-color: white;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        margin-top: 20px;
    }
    .fraud {
        color: #ff4b4b;
        font-weight: bold;
    }
    .legitimate {
        color: #00cc00;
        font-weight: bold;
    }
    .reasoning {
        background-color: #e8f4fc;
        padding: 15px;
        border-radius: 8px;
        margin-top: 15px;
    }
    .percentage-bar {
        height: 30px;
        background-color: #e0e0e0;
        border-radius: 15px;
        margin: 20px 0;
        overflow: hidden;
    }
    .percentage-fill {
        height: 100%;
        display: flex;
        align-items: center;
        justify-content: center;
        color: white;
        font-weight: bold;
    }
</style>
""", unsafe_allow_html=True)

# Header
st.markdown('<div class="header"><h1>🚨 Scam Message Predictor</h1><p>Powered by Llama-3.2-1B-Instruct</p></div>', unsafe_allow_html=True)

# Initialize session state
if 'model_loaded' not in st.session_state:
    st.session_state.model_loaded = False
    st.session_state.model = None
    st.session_state.tokenizer = None

@st.cache_resource
def load_model():
    """Load the Llama model and tokenizer"""
    try:
        # Updated path since model files are now in root directory
        model_path = "."
        tokenizer = AutoTokenizer.from_pretrained(model_path)
        
        # Set padding token if not already set
        if tokenizer.pad_token is None:
            tokenizer.pad_token = tokenizer.eos_token
            
        # Force GPU loading for RTX 4060
        if torch.cuda.is_available():
            st.info(f"Loading model on GPU: {torch.cuda.get_device_name(0)}")
            model = AutoModelForCausalLM.from_pretrained(
                model_path,
                torch_dtype=torch.float16,  # Use float16 for better GPU performance
                low_cpu_mem_usage=True,
                device_map={"": 0}  # Force loading on GPU 0 (RTX 4060)
            )
            st.success("Model successfully loaded on GPU!")
        else:
            st.error("No CUDA GPU detected. Cannot load model on GPU as requested.")
            return None, None
        
        model.eval()
        return model, tokenizer
    except Exception as e:
        st.error(f"Error loading model: {str(e)}")
        return None, None

# Automatically load model on app start since user has RTX 4060
if not st.session_state.model_loaded:
    with st.spinner("Loading Llama-3.2-1B-Instruct model on GPU... This may take a minute."):
        model, tokenizer = load_model()
        if model and tokenizer:
            st.session_state.model = model
            st.session_state.tokenizer = tokenizer
            st.session_state.model_loaded = True
            st.success("Model loaded successfully on GPU!")
        else:
            st.error("Failed to load model on GPU. Please check your CUDA installation.")

# Main app interface
if st.session_state.model_loaded and st.session_state.model is not None and st.session_state.tokenizer is not None:
    # Verify model is on GPU
    device = next(st.session_state.model.parameters()).device
    st.sidebar.success(f"✅ Model running on: {device}")
    
    # Create columns for layout
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.subheader("Enter Message for Fraud Analysis")
        user_input = st.text_area(
            "Paste the message you want to analyze:",
            height=200,
            placeholder="Enter the text message, email, or conversation to analyze for fraud..."
        )
        
        if st.button("🔍 Analyze for Fraud", use_container_width=True):
            if user_input.strip():
                with st.spinner("Analyzing message for fraud..."):
                    try:
                        # Create prompt for fraud analysis with detailed reasoning
                        prompt = f"""
<|begin_of_text|><|start_header_id|>system<|end_header_id|>
You are an expert fraud detection system. Analyze the following text and determine if it is fraudulent or legitimate. 
Provide your response in the following JSON format:
{{
    "classification": "FRAUD" or "LEGITIMATE",
    "fraud_percentage": a number between 0-100,
    "reasoning": "Detailed explanation of why this message is classified as fraud or legitimate, including specific red flags or indicators."
}}
<|eot_id|><|start_header_id|>user<|end_header_id|>
Analyze this text for fraud: {user_input}
<|eot_id|><|start_header_id|>assistant<|end_header_id|>
"""

                        # Tokenize input
                        inputs = st.session_state.tokenizer(
                            prompt, 
                            return_tensors="pt", 
                            truncation=True, 
                            padding=True
                        )

                        # Move to GPU (should already be on GPU, but just to be safe)
                        inputs = {k: v.to("cuda") for k, v in inputs.items()}

                        # Generate response
                        with torch.no_grad():
                            outputs = st.session_state.model.generate(
                                **inputs,
                                max_new_tokens=200,
                                do_sample=False,
                                temperature=0.0
                            )

                        # Decode response
                        response = st.session_state.tokenizer.decode(outputs[0], skip_special_tokens=True)
                        result_text = response.split("<|start_header_id|>assistant<|end_header_id|>")[-1].strip()
                        
                        # Parse the result (simplified parsing - in a real app, you'd want more robust JSON parsing)
                        st.markdown('<div class="result-card">', unsafe_allow_html=True)
                        
                        # Display classification
                        if "FRAUD" in result_text.upper():
                            st.markdown('<h2 class="fraud">🚨 FRAUD DETECTED</h2>', unsafe_allow_html=True)
                        else:
                            st.markdown('<h2 class="legitimate">✅ SEEMS LEGITIMATE</h2>', unsafe_allow_html=True)
                        
                        # Extract fraud percentage (simplified)
                        import re
                        percentage_match = re.search(r'(\d+)%', result_text)
                        if percentage_match:
                            fraud_percentage = int(percentage_match.group(1))
                        else:
                            fraud_percentage = 75 if "FRAUD" in result_text.upper() else 25
                        
                        # Display percentage bar
                        st.markdown(f"""
                        <div class="percentage-bar">
                            <div class="percentage-fill" style="width:{fraud_percentage}%;background-color:{'#ff4b4b' if fraud_percentage > 50 else '#00cc00'}">
                                {fraud_percentage}% Fraud Probability
                            </div>
                        </div>
                        """, unsafe_allow_html=True)
                        
                        # Display reasoning
                        st.markdown('<div class="reasoning">', unsafe_allow_html=True)
                        st.markdown("### Reasoning:")
                        if "reasoning" in result_text.lower():
                            # Extract reasoning part (simplified)
                            reasoning_start = result_text.lower().find("reasoning")
                            reasoning_text = result_text[reasoning_start:]
                            st.write(reasoning_text)
                        else:
                            st.write(result_text)
                        st.markdown('</div>', unsafe_allow_html=True)
                        
                        st.markdown('</div>', unsafe_allow_html=True)
                        
                    except Exception as e:
                        st.error(f"Error during analysis: {str(e)}")
            else:
                st.warning("Please enter a message to analyze.")
    
    with col2:
        st.subheader("ℹ️ About This Tool")
        st.markdown("""
        This tool uses Meta's Llama-3.2-1B-Instruct model to detect fraudulent messages.
        
        **How it works:**
        1. Enter a text message, email, or conversation
        2. The AI analyzes it for fraud indicators
        3. Results include fraud probability and detailed reasoning
        
        **Common fraud indicators:**
        - Requests for personal information
        - Urgent or threatening language
        - Suspicious links or attachments
        - Unusual payment requests
        - Impersonation of trusted entities
        """)
        
        st.subheader("📊 Fraud Detection Tips")
        st.markdown("""
        - Be cautious of unsolicited messages
        - Verify sender identity independently
        - Never share passwords or PINs
        - Check URLs carefully
        - Report suspicious messages
        """)
        
        if st.session_state.model_loaded:
            device = next(st.session_state.model.parameters()).device
            st.success(f"✅ Model running on: {device}")
            if torch.cuda.is_available():
                st.info(f"GPU: {torch.cuda.get_device_name(0)}")
else:
    st.info("Loading model on GPU... Please wait.")

# Footer
st.markdown("---")
st.caption("🚨 Scam Message Predictor - Using Llama-3.2-1B-Instruct for advanced fraud detection")
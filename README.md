# Scam Message Predictor

![Python](https://img.shields.io/badge/Python-3.8%2B-blue) ![License](https://img.shields.io/badge/License-MIT-green) ![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux%20%7C%20macOS-lightgrey)

An advanced scam message detection system powered by Meta's Llama-3.2-1B-Instruct model. This application analyzes text messages, emails, and conversations to identify potential fraud with detailed reasoning and fraud probability percentages.

## 🚀 Features

- **AI-Powered Fraud Detection**: Utilizes Llama-3.2-1B-Instruct for accurate scam detection
- **Real-time Analysis**: Instant fraud probability scoring and detailed reasoning
- **GPU Acceleration**: Supports CUDA-enabled GPUs for faster inference
- **User-Friendly Interface**: Streamlit-based web interface for easy interaction
- **Comprehensive Reporting**: Provides both fraud percentage and detailed analysis

## 📋 Requirements

- Python 3.8 or higher
- CUDA-compatible GPU (optional but recommended for faster performance)
- 8GB+ RAM (16GB+ recommended)
- 5GB+ free disk space

## 📥 Model Download

Due to the size of the model files, they are not included in this repository. Please download the Llama-3.2-1B-Instruct model files separately:

### Option 1: Manual Download
1. Download the Llama-3.2-1B-Instruct model files from Hugging Face:
   - Visit: https://huggingface.co/meta-llama/Llama-3.2-1B-Instruct
   - Download the following files:
     - config.json
     - model.safetensors
     - tokenizer.json
     - tokenizer_config.json
     - special_tokens_map.json
2. Place all files in the root directory of this project

### Option 2: Automatic Download (Coming Soon)
We're working on a script to automatically download the model files. For now, please use the manual method above.

## 🛠️ Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/scam-message-predictor.git
   cd scam-message-predictor
   ```

2. **Create a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Install PyTorch with CUDA support** (for GPU acceleration):
   ```bash
   pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
   ```

5. **Download model files** (see Model Download section above)

## ▶️ Usage

1. **Run the application**:
   ```bash
   streamlit run fraud_detection_app.py
   ```

2. **Open your browser** to the provided local URL (typically `http://localhost:8501`)

3. **Enter a message** in the text area and click "Analyze for Fraud"

## 🧠 How It Works

The system uses Meta's Llama-3.2-1B-Instruct model, a powerful language model fine-tuned for instruction following. When you input a message:

1. The text is processed and formatted for the Llama model
2. The model analyzes the content for fraud indicators
3. Results include:
   - Fraud probability percentage
   - Classification (Fraud/Legitimate)
   - Detailed reasoning with specific red flags

## 📊 Example Output

```
🚨 FRAUD DETECTED
75% Fraud Probability

### Reasoning:
This message contains several red flags:
- Impersonation of a bank security department
- Request for sensitive account information
- Urgent language creating pressure
- Overseas transaction claims without verification
```

## 🎯 Fraud Indicators Detected

- Phishing attempts
- Social engineering
- Financial scams
- Identity theft attempts
- Fake technical support
- Romance scams
- Lottery/sweepstakes fraud

## 📁 Project Structure

```
scam-message-predictor/
├── fraud_detection_app.py    # Main Streamlit application
├── download_model.py         # Model download script (coming soon)
├── config.json              # Model configuration (to be downloaded)
├── model.safetensors        # Model weights (to be downloaded)
├── tokenizer.json           # Tokenizer data (to be downloaded)
├── tokenizer_config.json    # Tokenizer configuration (to be downloaded)
├── special_tokens_map.json  # Special tokens mapping (to be downloaded)
├── requirements.txt         # Python dependencies
├── README.md               # This file
└── LICENSE                 # MIT License
```

## ⚙️ Technical Details

- **Model**: Llama-3.2-1B-Instruct (1B parameters)
- **Framework**: Hugging Face Transformers
- **Interface**: Streamlit
- **Precision**: float16 (GPU) / float32 (CPU)
- **Token Limit**: 200 new tokens for generation

## 📈 Performance

| Device | Loading Time | Inference Time (per message) |
|--------|--------------|------------------------------|
| RTX 4060 GPU | ~30 seconds | ~2-3 seconds |
| CPU (i7) | ~1 minute | ~10-15 seconds |

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

The Llama-3.2-1B-Instruct model is licensed under the [Meta Llama 3.2 Community License](https://llama.meta.com/llama3_2/license/).

## 🙏 Acknowledgments

- Meta for releasing the Llama-3.2-1B-Instruct model
- Hugging Face for the Transformers library
- Streamlit for the web interface framework

## 📧 Contact

Your Name - [@your_twitter](https://twitter.com/your_twitter) - your.email@example.com

Project Link: [https://github.com/yourusername/scam-message-predictor](https://github.com/yourusername/scam-message-predictor)
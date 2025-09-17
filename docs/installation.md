# Installation Guide

## System Requirements

### Minimum Requirements
- Python 3.8 or higher
- 8GB RAM
- 5GB free disk space

### Recommended Requirements
- Python 3.10 or higher
- 16GB RAM
- CUDA-compatible GPU (RTX 3060 or better recommended)
- 10GB free disk space

## Step-by-Step Installation

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/scam-message-predictor.git
cd scam-message-predictor
```

### 2. Create a Virtual Environment

It's recommended to use a virtual environment to avoid conflicts with other Python projects:

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Download Model Files

Due to the size of the model files, they are not included in the repository. You need to download them separately:

#### Manual Download:
1. Visit the Hugging Face model page: https://huggingface.co/meta-llama/Llama-3.2-1B-Instruct
2. Download the following files:
   - config.json
   - model.safetensors
   - tokenizer.json
   - tokenizer_config.json
   - special_tokens_map.json
3. Place all files in the root directory of this project

### 5. Install PyTorch with CUDA Support (For GPU Acceleration)

If you have a CUDA-compatible GPU, install PyTorch with CUDA support for significantly faster inference:

```bash
# Uninstall CPU-only version if already installed
pip uninstall torch torchvision torchaudio

# Install CUDA-enabled version
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
```

### 6. Verify Installation

Check if CUDA is properly configured:

```bash
python -c "import torch; print('CUDA available:', torch.cuda.is_available()); print('CUDA version:', torch.version.cuda)"
```

## Troubleshooting

### Common Issues

1. **Import Errors**: Make sure all dependencies are installed:
   ```bash
   pip install -r requirements.txt
   ```

2. **CUDA Not Detected**: 
   - Verify your GPU is CUDA-compatible
   - Install proper NVIDIA drivers
   - Reinstall PyTorch with CUDA support

3. **Memory Errors**: 
   - Close other applications
   - Consider using CPU mode for lower memory consumption

4. **Model Files Not Found**:
   - Ensure all model files are downloaded and placed in the root directory
   - Check that file names match exactly

### Windows-Specific Issues

1. **Microsoft Visual C++ 14.0 Required**:
   Install Microsoft C++ Build Tools from https://visualstudio.microsoft.com/visual-cpp-build-tools/

2. **Long Path Issues**:
   Enable long path support in Windows Group Policy or Registry

## Updating the Application

To update to the latest version:

```bash
git pull
pip install -r requirements.txt --upgrade
```

Note: Model files will not be updated through git pull and must be manually updated if needed.
# Project Directory Structure

This document explains the organization of files and directories in the Scam Message Predictor project.

## Root Directory

```
scam-message-predictor/
├── docs/                   # Documentation files
├── .gitignore             # Git ignore file
├── Interface.png          # Application interface screenshot
├── LICENSE                # Project license
├── README.md              # Main project documentation
├── config.json            # Model configuration (to be downloaded)
├── fraud_detection_app.py # Main application file
├── download_model.py      # Model download script (coming soon)
├── model.safetensors      # Model weights (to be downloaded)
├── requirements.txt       # Python dependencies
├── special_tokens_map.json# Special token mappings (to be downloaded)
├── tokenizer.json         # Tokenizer data (to be downloaded)
└── tokenizer_config.json  # Tokenizer configuration (to be downloaded)
```

## Documentation Directory

```
docs/
├── contributing.md        # Contribution guidelines
├── directory_structure.md # This file
├── installation.md        # Installation instructions
├── model_info.md          # Model information
└── usage.md              # Usage instructions
```

## Detailed File Descriptions

### Main Application Files

#### [fraud_detection_app.py](file:///d:/Scam-Message-Prediction/fraud_detection_app.py)
The main Streamlit application that provides the web interface for fraud detection.

#### [download_model.py](file:///d:/Scam-Message-Prediction/download_model.py)
Script to download model files (work in progress).

#### [requirements.txt](file:///d:/Scam-Message-Prediction/requirements.txt)
Lists all Python package dependencies required to run the application.

#### [config.json](file:///d:/Scam-Message-Prediction/config.json) (to be downloaded)
Contains the model architecture configuration parameters.

#### [model.safetensors](file:///d:/Scam-Message-Prediction/model.safetensors) (to be downloaded)
Contains the model weights in the safe tensor format (2.4GB).

#### [tokenizer.json](file:///d:/Scam-Message-Prediction/tokenizer.json) (to be downloaded)
Contains the tokenizer data used to convert text to tokens (8.8MB).

#### [tokenizer_config.json](file:///d:/Scam-Message-Prediction/tokenizer_config.json) (to be downloaded)
Configuration file for the tokenizer.

#### [special_tokens_map.json](file:///d:/Scam-Message-Prediction/special_tokens_map.json) (to be downloaded)
Maps special tokens used by the model.

### Documentation Files

#### [README.md](file:///d:/Scam-Message-Prediction/README.md)
Main project documentation with overview, installation, and usage instructions.

#### [LICENSE](file:///d:/Scam-Message-Prediction/LICENSE)
Project license information.

#### [Interface.png](file:///d:/Scam-Message-Prediction/Interface.png)
Screenshot of the application interface.

#### [docs/installation.md](file:///d:/Scam-Message-Prediction/docs/installation.md)
Detailed installation instructions and troubleshooting.

#### [docs/usage.md](file:///d:/Scam-Message-Prediction/docs/usage.md)
Comprehensive usage guide with examples.

#### [docs/model_info.md](file:///d:/Scam-Message-Prediction/docs/model_info.md)
Technical information about the Llama model.

#### [docs/contributing.md](file:///d:/Scam-Message-Prediction/docs/contributing.md)
Guidelines for contributing to the project.

#### [docs/directory_structure.md](file:///d:/Scam-Message-Prediction/docs/directory_structure.md)
This file explaining the project structure.

### Configuration Files

#### [.gitignore](file:///d:/Scam-Message-Prediction/.gitignore)
Specifies files and directories that should not be tracked by Git.

## File Size Summary

| File | Size | Description |
|------|------|-------------|
| [model.safetensors](file:///d:/Scam-Message-Prediction/model.safetensors) | 2.4 GB | Model weights (to be downloaded) |
| [tokenizer.json](file:///d:/Scam-Message-Prediction/tokenizer.json) | 8.8 MB | Tokenizer data (to be downloaded) |
| [tokenizer_config.json](file:///d:/Scam-Message-Prediction/tokenizer_config.json) | 53 KB | Tokenizer configuration (to be downloaded) |
| [Interface.png](file:///d:/Scam-Message-Prediction/Interface.png) | 78 KB | Interface screenshot |
| All other files | < 100 KB each | Configuration and code |

## Important Notes

1. **Model Files**: The large model files are not included in the repository and must be downloaded separately.

2. **Git Tracking**: Large files are excluded via [.gitignore](file:///d:/Scam-Message-Prediction/.gitignore) to keep the repository size manageable.

3. **Backup**: Always backup the model files after downloading them.

4. **Portability**: The project is designed to be portable - all necessary files can be downloaded and organized in the repository structure.

5. **Dependencies**: The [requirements.txt](file:///d:/Scam-Message-Prediction/requirements.txt) file ensures consistent dependency management across different environments.

6. **Download Script**: A script to automatically download model files is in development.
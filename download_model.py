"""
Script to download Llama-3.2-1B-Instruct model files
"""

import os
import requests
from tqdm import tqdm

def download_file(url, filename):
    """
    Download a file from a URL with progress bar
    """
    print(f"Downloading {filename}...")
    
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()
        
        # Get total file size
        total_size = int(response.headers.get('content-length', 0))
        
        with open(filename, 'wb') as file, tqdm(
            desc=filename,
            total=total_size,
            unit='B',
            unit_scale=True,
            unit_divisor=1024,
        ) as progress_bar:
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:
                    file.write(chunk)
                    progress_bar.update(len(chunk))
        
        print(f"Downloaded {filename} successfully!")
        return True
        
    except Exception as e:
        print(f"Error downloading {filename}: {str(e)}")
        return False

def main():
    """
    Download all required model files
    """
    # Create directory for model files if it doesn't exist
    os.makedirs("model_files", exist_ok=True)
    
    # Model files to download (these would be the actual URLs)
    model_files = {
        "config.json": "https://example.com/config.json",
        "model.safetensors": "https://example.com/model.safetensors",
        "tokenizer.json": "https://example.com/tokenizer.json",
        "tokenizer_config.json": "https://example.com/tokenizer_config.json",
        "special_tokens_map.json": "https://example.com/special_tokens_map.json"
    }
    
    print("Downloading Llama-3.2-1B-Instruct model files...")
    print("This will download approximately 3GB of data.")
    
    success_count = 0
    for filename, url in model_files.items():
        if download_file(url, os.path.join("model_files", filename)):
            success_count += 1
    
    print(f"\nDownload complete! {success_count}/{len(model_files)} files downloaded successfully.")
    print("Please move the files from the 'model_files' directory to the project root directory.")

if __name__ == "__main__":
    main()
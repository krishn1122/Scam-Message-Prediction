# Model Information

## Llama-3.2-1B-Instruct

This project utilizes Meta's Llama-3.2-1B-Instruct model, a powerful language model optimized for instruction following and text analysis tasks.

### Model Specifications

- **Parameters**: 1 Billion
- **Architecture**: Transformer-based
- **Training**: Instruction fine-tuned
- **Context Length**: Up to 131,072 tokens
- **Languages**: Multilingual support (optimized for English)

### Why Llama-3.2-1B-Instruct?

1. **Efficiency**: Smaller than larger models but still highly capable
2. **Local Execution**: Can run entirely on consumer hardware
3. **Instruction Following**: Fine-tuned to understand and follow complex instructions
4. **Fraud Detection Capabilities**: Excellent at identifying suspicious patterns in text

### Model Files

Due to the large size of the model files, they are not included in this repository. You will need to download them separately:

1. **config.json**: Model architecture configuration
2. **model.safetensors**: Model weights (2.4GB)
3. **tokenizer.json**: Tokenizer data (8.8MB)
4. **tokenizer_config.json**: Tokenizer configuration
5. **special_tokens_map.json**: Special token mappings

### Download Instructions

See the main [README.md](file:///d:/Scam-Message-Prediction/README.md) file for detailed instructions on downloading the model files.

### Model Loading

The model is loaded using Hugging Face Transformers library with optimizations:

```python
model = AutoModelForCausalLM.from_pretrained(
    model_path,
    torch_dtype=torch.float16,  # Reduced precision for GPU
    low_cpu_mem_usage=True,     # Memory optimization
    device_map={"": 0}          # Force GPU loading
)
```

### Prompt Engineering

The application uses carefully crafted prompts to guide the model's fraud detection capabilities:

```
<|begin_of_text|><|start_header_id|>system<|end_header_id|>
You are an expert fraud detection system. Analyze the following text and determine if it is fraudulent or legitimate. 
Provide your response in the following JSON format:
{
    "classification": "FRAUD" or "LEGITIMATE",
    "fraud_percentage": a number between 0-100,
    "reasoning": "Detailed explanation of why this message is classified as fraud or legitimate, including specific red flags or indicators."
}
<|eot_id|><|start_header_id|>user<|end_header_id|>
Analyze this text for fraud: {user_input}
<|eot_id|><|start_header_id|>assistant<|end_header_id|>
```

### Performance Characteristics

#### Loading Time
- **GPU (RTX 4060)**: ~30 seconds
- **CPU (i7)**: ~1 minute

#### Inference Time
- **GPU (RTX 4060)**: 2-3 seconds per message
- **CPU (i7)**: 10-15 seconds per message

#### Memory Usage
- **GPU**: ~4-6GB VRAM
- **CPU**: ~6-8GB RAM

### Model Limitations

1. **False Positives**: May occasionally flag legitimate messages as fraudulent
2. **False Negatives**: Sophisticated scams might not be detected
3. **Language Bias**: Primarily optimized for English text
4. **Context Limitations**: Analyzes messages in isolation without external verification

### Model Updates

To update the model, you would need to:
1. Download the latest Llama-3.2-1B-Instruct files
2. Replace the existing model files
3. Verify compatibility with the application code

Note: Always backup your current model files before updating.
# Usage Guide

## Running the Application

After completing the installation, you can run the Scam Message Predictor application:

```bash
streamlit run fraud_detection_app.py
```

The application will start and provide a local URL (typically `http://localhost:8501`). Open this URL in your web browser to access the interface.

## Interface Overview

### Main Analysis Panel

1. **Text Input Area**: Paste or type the message you want to analyze
2. **Analyze Button**: Click to start the fraud detection process
3. **Results Display**: Shows fraud probability, classification, and reasoning

### Information Panel

1. **About This Tool**: Explains how the system works
2. **Fraud Detection Tips**: Provides general advice on identifying scams
3. **Device Information**: Shows whether the model is running on CPU or GPU

## Analyzing Messages

### 1. Input Your Message

Paste or type the text you want to analyze in the text area. This can be:
- Email content
- Text messages
- Chat conversations
- Social media messages
- Any text you suspect might be fraudulent

### 2. Click "Analyze for Fraud"

The system will process your message and provide:
- **Fraud Probability**: A percentage indicating how likely the message is fraudulent
- **Classification**: Clear "FRAUD DETECTED" or "SEEMS LEGITIMATE" determination
- **Reasoning**: Detailed explanation of why the message was classified as such

### 3. Review Results

The results include:
- Visual percentage bar showing fraud likelihood
- Color-coded classification (red for fraud, green for legitimate)
- Detailed reasoning with specific red flags identified

## Example Analyses

### Fraud Example

```
Message: "Congratulations! You've won $1,000,000 in our lottery! Click this link to claim your prize: [suspicious-link.com]. You just need to pay a small processing fee of $500 first."

Result:
🚨 FRAUD DETECTED
85% Fraud Probability

Reasoning: This message contains classic lottery scam indicators including unexpected winnings, requests for payment to receive prize, and suspicious links.
```

### Legitimate Example

```
Message: "Hi John, just wanted to confirm our meeting tomorrow at 2 PM in Conference Room B. Looking forward to it!"

Result:
✅ SEEMS LEGITIMATE
15% Fraud Probability

Reasoning: This appears to be a normal workplace communication with no fraud indicators present.
```

## Performance Considerations

### GPU vs CPU Performance

- **GPU (CUDA)**: 2-3 seconds per analysis
- **CPU**: 10-15 seconds per analysis

### Memory Usage

The application typically uses 4-6GB of RAM during operation. Ensure your system has sufficient free memory.

## Best Practices

1. **Provide Complete Messages**: Include the full text for most accurate analysis
2. **Check Regularly**: Analyze suspicious messages immediately when received
3. **Verify Results**: Use the system as one tool among many for fraud detection
4. **Report Scams**: Report confirmed fraud attempts to appropriate authorities

## Privacy and Security

- All processing happens locally on your machine
- No data is sent to external servers
- Messages are not stored or logged by the application
- Model weights are stored locally and never transmitted
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

# Load the tokenizer and the model from Hugging Face
tokenizer = AutoTokenizer.from_pretrained("austinb/fraud_text_detection")
model = AutoModelForSequenceClassification.from_pretrained(
    "austinb/fraud_text_detection"
)

# Set model to evaluation mode
model.eval()

# Sample transcript text
transcript = """Hi, this is John from XYZ bank security department. We are calling to inform you that we have been suspicious activities on your account Are you aware of any recent transaction? We have noticed a charge of $1,200 made at overseas location just for a few hours ago It's a huge and suspicious and we want to ensure it wasn't you who made this purchase Alright, no worries. We can block this transaction for you But before we proceed I need to verify some information for security purpose Could you please confirm the last four digits of your bank account number? Thank you.Now, I just make sure that we cancel the transaction immediately"""

# Tokenize the input
inputs = tokenizer(transcript, return_tensors="pt", truncation=True, padding=True)

# Get model predictions
with torch.no_grad():
    outputs = model(**inputs)
    logits = outputs.logits

# Get predicted label (assuming binary classification, 0: not fraud, 1: fraud)
predicted_label = torch.argmax(logits, dim=-1).item()

if predicted_label == 1:
    print("The transcript is fraudulent.")
else:
    print("The transcript is not fraudulent.")

import pandas as pd
from transformers import BertTokenizer, BertForQuestionAnswering
import torch

# Load the pre-trained DistilBERT model and tokenizer
model_name = "bert-large-uncased"
tokenizer = BertTokenizer.from_pretrained(model_name)
model = BertForQuestionAnswering.from_pretrained(model_name)

# Load the CSV data into a pandas DataFrame
csv_file = "chatbot_test.csv"  # Replace with the path to your CSV file
df = pd.read_csv(csv_file)

def create_context(row):
    return f"Date: {row['Date']}, Open: {row['Open']}, High: {row['High']}, Low: {row['Low']}, Close: {row['Close']}, Volume: {row['Volume']}, OI: {row['OI']}. "

def process_question(question):
    context = ""
    for _, row in df.iterrows():
        context += create_context(row)

    inputs = tokenizer(question, context, return_tensors="pt")
    start_scores, end_scores = model(**inputs)
    start_index = torch.argmax(start_scores)
    end_index = torch.argmax(end_scores) + 1
    answer = tokenizer.convert_tokens_to_string(tokenizer.convert_ids_to_tokens(inputs["input_ids"][0][start_index:end_index]))
    return answer

# Example usage
question = "What was the closing price on 2019-04-01 at 09:16?"
answer = process_question(question)
print("Answer:", answer)

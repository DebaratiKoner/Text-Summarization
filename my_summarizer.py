from transformers import pipeline

# Abstractive summarizer
abstractive_summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def abstractive_summary(text):
    summary = abstractive_summarizer(text, max_length=150, min_length=40, do_sample=False)
    return summary[0]['summary_text']

# Extractive summarizer using Huggingface (example)
from summarizer import Summarizer

def extractive_summary(text):
    model = Summarizer()
    result = model(text, min_length=60)
    return result

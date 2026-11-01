"""Inspectable caption features, independent of model training."""
from collections import Counter
from src.preprocessing.text import clean_caption

def token_counts(captions):
    return Counter(token.lower() for caption in captions for token in clean_caption(caption).split())

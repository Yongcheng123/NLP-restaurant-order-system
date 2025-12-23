"""Configuration settings for the restaurant ordering chatbot."""
import os

# NLP Model Configuration
SPACY_MODEL = os.environ.get('SPACY_MODEL', 'en_core_web_md')
BERT_MODEL = os.environ.get('BERT_MODEL', 'vblagoje/bert-english-uncased-finetuned-pos')

# Data Files
MENU_CSV = os.environ.get('MENU_CSV', 'menu.csv')
DATA_CSV = os.environ.get('DATA_CSV', 'data.csv')

# NLU Configuration
SIMILARITY_THRESHOLD = 0.6

# Spice Level Options
SPICE_LEVELS = {
    'mild': ['none', 'nothing', 'mild', 'not', 'tame', 'minimum'],
    'medium': ['medium', 'middle', 'mediocre'],
    'spicy': ['spicy', 'hot', 'intense', 'burn', 'maximum']
}

# Number Words (excluded from stop words)
NUMBER_WORDS = [
    'none', 'nothing', 'twenty', 'eight', 'two', 'hundred', 'one', 'five',
    'four', 'six', 'three', 'ten', 'fifty', 'nine', 'twelve'
]

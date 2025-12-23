# Restaurant Ordering System

A bilingual (English/Chinese) restaurant ordering chatbot with natural language understanding capabilities. The system supports both web-based and command-line interfaces for taking food orders.

## Features

- **Bilingual Support**: Processes orders in both English and Chinese
- **Natural Language Understanding**: Uses spaCy and transformers for intent recognition and entity extraction
- **Voice Interface**: Speech-to-text input and text-to-speech output
- **Menu Management**: Query menu items, add/remove items from orders
- **Web Interface**: Flask-based UI with real-time interaction
- **Smart Order Processing**: Handles quantities, customization (spice levels), and drinks

## Prerequisites

- Python 3.8+
- MySQL (for pattern library dependency)
- spaCy English model: `en_core_web_md`

## Installation

1. Clone the repository:
```bash
git clone https://github.com/Yongcheng123/NLP-restaurant-order-system.git
cd NLP-restaurant-order-system
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
python -m spacy download en_core_web_md
```

## Usage

### Web Application

Start the Flask server:
```bash
python run_webapp.py
```

Then navigate to `http://localhost:5000` in your browser.

### Command Line Interface

Run the chatbot directly:
```bash
python run_chatbot.py
```

## Project Structure

```
├── src/
│   ├── chatbot/              # Core chatbot logic
│   │   ├── config.py         # Configuration settings
│   │   ├── core/             # Core NLU and dialog
│   │   │   ├── nlu.py        # Natural language understanding
│   │   │   ├── dialog_manager.py  # Dialog flow management
│   │   │   └── actions.py    # Order processing actions
│   │   └── services/         # External services
│   │       ├── translation.py  # Language translation
│   │       └── speech.py     # Speech I/O
│   └── webapp/               # Web application
│       ├── app/              # Flask application
│       └── actions.py        # Web-specific handlers
├── data/                     # Data files
│   ├── menu.csv             # Restaurant menu
│   └── data.csv             # Training data
├── docs/                     # Documentation
├── examples/                 # Usage examples
├── run_chatbot.py           # CLI entry point
└── run_webapp.py            # Web app entry point
```

## Supported Commands

- **Add items**: "I want to order fried rice" / "我要点炒饭"
- **Remove items**: "Remove the soup from my order"
- **Query menu**: "What dishes do you have?" / "Show me the menu"
- **Complete order**: "That's all" / "Checkout"

## Technical Stack

- **NLP**: spaCy, Transformers (BERT)
- **Web**: Flask
- **Speech**: gTTS, SpeechRecognition
- **Data**: pandas, scikit-learn

## Development

This project was developed as part of an NLP course project, focusing on practical applications of natural language processing in real-world scenarios.

## License

MIT License - see LICENSE file for details

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

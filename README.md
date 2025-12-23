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
git clone <repository-url>
cd NLP-project
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
flask --app flask-webapp run
```

Then navigate to `http://localhost:5000` in your browser.

### Command Line Interface

Run the chatbot directly:
```bash
python MenuTranslationAssistant.py
```

## Project Structure

```
├── flask-webapp/          # Web application
│   ├── static/           # CSS, JS, images
│   └── templates/        # HTML templates
├── nlu.py                # Natural language understanding
├── task_manager.py       # Dialog management
├── assistant_actions.py  # Order processing logic
├── web_actions.py        # Web-specific handlers
├── machine_translation.py # Translation utilities
├── speech_text.py        # Voice I/O
├── data.csv              # Training data
└── menu.csv              # Restaurant menu
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

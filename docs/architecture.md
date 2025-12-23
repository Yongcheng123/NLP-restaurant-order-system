# System Architecture

## Overview

The Restaurant Ordering System is built with a modular architecture separating concerns between NLU, dialog management, and presentation layers. The codebase is organized into clear packages for maintainability and scalability.

## Directory Structure

```
src/
├── chatbot/                 # Core chatbot functionality
│   ├── config.py           # Centralized configuration
│   ├── core/               # Core business logic
│   │   ├── nlu.py         # Natural Language Understanding
│   │   ├── dialog_manager.py  # Conversation flow management
│   │   └── actions.py     # Order processing actions
│   ├── services/           # External service integrations
│   │   ├── translation.py # Machine translation
│   │   └── speech.py      # Speech recognition/synthesis
│   └── models/             # Data models (future)
└── webapp/                src/chatbot/core/dialogWeb application
    ├── app/                # Flask application
    │   ├── __init__.py    # App factory
    │   ├── static/        # CSS, JS, images
    │   └── templates/     # HTML templates
    └── actions.py          # Web-specific handlers

data/                        # Data files
├── menu.csv                # Restaurant menu
└── data.csv                # Training/reference data

run_chatbot.py              # CLI entry point
run_webapp.py               # Web app entry point
```

## Components

### 1. Natural Language Understanding (`src/chatbot/core/nlu.py`)

Handles intent recognition and entity extraction using:
- spaCy for NLP processing and similarity matching
- BERT-based token classification for POS tagging
- Semantic similarity for menu item matching

**Key Functions:**
- `identifyAction()`: Maps tokens to action intents (add/remove/query/complete)
- `fillAction()`: Extracts action from POS-tagged tokens
- `fillItem()`: Identifies menu items and quantities from user input

### 2. Dialog Management (`task_manager.py`)

Manages conversation flow and slot filling:
- Tracks order state across turns
- Prompts for missing information (spice level, drinks)
- Handles bilingual interactions

**Slot Structure:**
```python
slots = [action, items, quantities, spice_level, drink]
```

### 3. Assistant Actions (`src/chatbot/core/actions.py`)

Executes user commands:
- `addOrder()`: Adds items to the cart
- `removeOrder()`: Removes items from cart
- `queryMenu()`: Searches menu
- `completeOrder()`: Finalizes transaction

### 4. Web Interface (`src/webapp/`)

Flask application providing:
- Real-time chat interface
- Dynamic menu rendering
- Shopping cart management
- Checkout flow

### 5. Translation (`src/chatbot/services/translation.py`)

Handles bilingual support for English and Chinese.

### 6. Speech Interface (`src/chatbot/services/speech.py`)

Provides voice I/O capabilities using:
- Google Text-to-Speech (gTTS)
- SpeechRecognition library

## Data Flow

```
User Input → NLU → Dialog Manager → Action Handler → Response
     ↓
Translation/Speech Processing (if needed)
```

## Configuration

Centralized configuration in `src/chatbot/config.py`:
- Model settings
- File paths (now in data/ directory)
- NLU thresholds
- Spice level mappings

All paths are configurable via environment variables for different deployment scenarios.

## Extension Points

- Add new intents in `src/chatbot/core/nlu.py` action lists
- Extend menu items in `data/menu.csv`
- Add language support in `src/chatbot/services/translation.py`
- Customize UI in Flask templates under `src/webapp/app/templates/`

## Benefits of New Structure

1. **Clear Separation**: Core logic separated from web interface
2. **Easier Testing**: Each module can be tested independently
3. **Scalability**: Easy to add new interfaces (mobile app, API)
4. **Maintainability**: Related code grouped together
5. **Professional**: Follows Python package best practices

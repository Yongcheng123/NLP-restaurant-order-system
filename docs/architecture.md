# System Architecture

## Overview

The Restaurant Ordering System is built with a modular architecture separating concerns between NLU, dialog management, and presentation layers.

## Components

### 1. Natural Language Understanding (`nlu.py`)

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

### 3. Assistant Actions (`assistant_actions.py`)

Executes user commands:
- `addOrder()`: Adds items to the cart
- `removeOrder()`: Removes items from cart
- `queryMenu()`: Searches menu
- `completeOrder()`: Finalizes transaction

### 4. Web Interface (`flask-webapp/`)

Flask application providing:
- Real-time chat interface
- Dynamic menu rendering
- Shopping cart management
- Checkout flow

### 5. Translation (`machine_translation.py`)

Handles bilingual support for English and Chinese.

### 6. Speech Interface (`speech_text.py`)

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

Centralized configuration in `config.py`:
- Model settings
- File paths
- NLU thresholds
- Spice level mappings

## Extension Points

- Add new intents in `nlu.py` action lists
- Extend menu items in `menu.csv`
- Add language support in `machine_translation.py`
- Customize UI in Flask templates

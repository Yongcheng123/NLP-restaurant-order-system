# API Documentation

## Flask Web API

### Endpoints

#### `GET /`
Home page with chat interface.

**Response:** HTML page with menu and chat UI

#### `POST /submit-prompt`
Process user chat message.

**Request Body:**
```json
{
  "textPrompt": "I want to order fried rice"
}
```

**Response:** HTML fragments containing:
- Sent message bubble
- Received response bubble(s)
- Cart updates (if applicable)

**Actions Supported:**
- `add`: Add items to order
- `remove`: Remove items from order
- `query`: Search menu
- `complete`: Proceed to checkout

## Command Line Interface

### Functions

#### `assist(slots, orders, menu_items, nlp, classifier, language, data)`
Main dialog management function.

**Parameters:**
- `slots`: Current slot values [action, items, quantities, spice, drink]
- `orders`: Current order list
- `menu_items`: Available menu items
- `nlp`: spaCy language model
- `classifier`: BERT token classifier
- `language`: Current language ('en' or 'zh-cn')
- `data`: Training data

**Returns:** `(request, slots, language)`

## NLU Functions

### `identifyAction(nlp, token)`
Identifies action intent from a token.

**Parameters:**
- `nlp`: spaCy model
- `token`: Input token string

**Returns:** `(action, confidence_score)`
- `action`: One of ['add', 'replace', 'remove', 'query', 'complete', 'none']
- `confidence_score`: Similarity score (0-1)

### `fillItem(slots, nlp, menu_items, response)`
Extracts menu items from natural language.

**Parameters:**
- `slots`: Current slot values
- `nlp`: spaCy model
- `menu_items`: List of menu items
- `response`: User input text

**Returns:** Updated slots with identified items and quantities

## Configuration

All configuration can be set via environment variables (see `.env.example`) or will use defaults from `config.py`.

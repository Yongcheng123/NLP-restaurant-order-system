# Usage Examples

## Web Interface Examples

### Starting the Server

```bash
# Set up environment (optional)
export SECRET_KEY="your-secret-key-here"

# Run the Flask app
python run_webapp.py

# Access at http://localhost:5000
```

### Example Interactions

**Adding Items:**
```
User: "I'd like to order kung pao chicken"
Bot: [Shows kung pao chicken options]
User: "Make it spicy with a cola"
Bot: "Added to your order!"
```

**Querying Menu:**
```
User: "What soups do you have?"
Bot: [Lists available soups from menu]
```

**Removing Items:**
```
User: "Remove the soup from my order"
Bot: "Removed soup from your order"
```

**Checking Out:**
```
User: "I'm done"
Bot: [Shows checkout page with order summary]
```

## Command Line Interface Examples

### Running the CLI

```bash
python run_chatbot.py
```

### Sample Session

```
Bot: How can I be of assistance?
     我可以帮你吗

You: I want fried rice

Bot: How spicy do you want it?

You: Medium

Bot: Do you want something to drink?

You: Yes

Bot: What do you want to drink?

You: Coke

Bot: How else can I help?

You: That's all

Bot: You ordered:
     - Fried Rice (Medium) x1
     - Coke x1
     Total: $12.50
     Is this correct?

You: Yes

Bot: Thank you for eating with us today!
```

## Bilingual Example

```
User: 我要点炒饭 (I want fried rice)
Bot: 您想要多辣？ (How spicy do you want it?)
User: 中辣 (Medium)
Bot: 要喝点什么吗？ (Want something to drink?)
User: 不用了 (No thanks)
Bot: 还需要什么吗？ (What else do you need?)
```

## API Usage Examples

### Direct Function Calls

```python
import spacy
from transformers import pipeline
from src.chatbot.core import nlu
from src.chatbot import config

# Load models
nlp = spacy.load(config.SPACY_MODEL)
classifier = pipeline("token-classification", model=config.BERT_MODEL)

# Identify action
action, score = nlu.identifyAction(nlp, "order")
print(f"Action: {action}, Confidence: {score}")
# Output: Action: add, Confidence: 0.95

# Fill slots from user input
slots = ["none", [], [], "", 0]
tokens = classifier("I want two fried rice")
slots = nlu.fillAction(slots, tokens, nlp)
print(slots)
# Output: ['add', [], [], '', 0]
```

## Testing the System

### Test Data

Create test scenarios in a Python script:

```python
test_cases = [
    "I'd like kung pao chicken",
    "Make it extra spicy",
    "Add sweet and sour pork",
    "What drinks do you have?",
    "Remove the pork",
    "I'm done"
]

# Process each test case
for test in test_cases:
    print(f"Input: {test}")
    # Process through your system
    # Verify expected output
```

### Menu Customization

Edit `data/menu.csv` to add your own items:

```csv
id,code,name,category,price
1,FR01,Fried Rice,Main,8.99
2,KC01,Kung Pao Chicken,Main,12.99
...
```

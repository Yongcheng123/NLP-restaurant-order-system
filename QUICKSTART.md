# Quick Start Guide

Get up and running with the Restaurant Ordering System in 5 minutes.

## Prerequisites

- Python 3.8 or higher
- pip package manager
- MySQL (for pattern library)

## Installation

```bash
# Clone the repository
git clone https://github.com/Yongcheng123/NLP-restaurant-order-system.git
cd NLP-project

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Download spaCy model
python -m spacy download en_core_web_md
```

## Run the Web App

```bash
# Set environment variable (optional, uses default otherwise)
export SECRET_KEY="your-production-secret-key"

# Start the server
python run_webapp.py

# Open browser to http://localhost:5000
```

## Run Command Line Version

```bash
python run_chatbot.py
```

## Basic Commands

| Action | Example |
|--------|---------|
| Order food | "I want fried rice" |
| Check menu | "Show me the menu" / "What soups do you have?" |
| Customize | "Make it spicy" |
| Add drink | "I'll have a coke" |
| Remove item | "Remove the soup" |
| Checkout | "That's all" / "I'm done" |

## Bilingual Support

The system automatically detects and responds in English or Chinese:

- English: "I want to order kung pao chicken"
- Chinese: "我要点宫保鸡丁"

## Configuration

Copy `.env.example` to `.env` and customize:

```bash
cp .env.example .env
# Edit .env with your settings
```

## Need Help?

- Check [docs/api.md](docs/api.md) for API details
- See [examples/usage_examples.md](examples/usage_examples.md) for more examples
- Read [docs/architecture.md](docs/architecture.md) to understand the system

## Troubleshooting

**Issue:** spaCy model not found  
**Solution:** Run `python -m spacy download en_core_web_md`

**Issue:** Pattern library installation fails  
**Solution:** Ensure MySQL is installed and configured

**Issue:** Port 5000 already in use  
**Solution:** Use `flask --app flask-webapp run --port 8000`

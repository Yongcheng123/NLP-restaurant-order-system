# Contributing to Restaurant Ordering System

Thank you for considering contributing to this project! Here are some guidelines to help you get started.

## Development Setup

1. Fork the repository and clone your fork
2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate
   ```
3. Install dependencies including dev tools:
   ```bash
   pip install -e ".[dev]"
   python -m spacy download en_core_web_md
   ```

## Code Style

This project follows Python best practices:

- Use [Black](https://black.readthedocs.io/) for code formatting
- Follow PEP 8 style guidelines
- Write meaningful variable names (snake_case for variables and functions)
- Add docstrings to functions and classes
- Keep functions focused and modular

Run formatting before committing:
```bash
black .
```

## Testing

Before submitting a PR, ensure:
- All existing functionality works
- New features are tested manually
- Code passes basic linting checks

## Pull Request Process

1. Create a new branch for your feature: `git checkout -b feature-name`
2. Make your changes with clear commit messages
3. Update documentation if needed
4. Push to your fork and submit a pull request
5. Describe your changes and their purpose in the PR description

## Areas for Contribution

- Improving NLU accuracy
- Adding more language support
- Enhancing the web UI
- Adding unit tests
- Improving error handling
- Documentation improvements

## Questions?

Feel free to open an issue for discussion before starting major work.

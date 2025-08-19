# Text Processing Application

A modular Python application for processing text files using AI completions.

## Project Structure

```
src/
├── main.py              # Main entry point - run this file
├── config.py            # Configuration settings and constants
├── prompts.py           # System prompts for AI models
├── api_client.py        # API client for OpenAI interactions
├── file_handler.py      # File I/O operations
├── retry_handler.py     # Retry logic for API failures
├── processor.py         # Main processing workflow orchestrator
├── requirements.txt     # Python dependencies
└── README.md           # This file
```

## Features

- **Modular Architecture**: Clean separation of concerns across multiple modules
- **Retry Logic**: Handles API rate limits with exponential backoff
- **Token Management**: Automatic token refresh on rate limit errors
- **File Processing**: Batch processing of text files in subdirectories
- **Excel Output**: Results saved to organized Excel files
- **Error Handling**: Robust error handling and logging

## How to Run

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Update your API token in `config.py`:
   ```python
   TOKEN = "your_actual_token_here"
   ```

3. Run the application:
   ```bash
   python main.py
   ```

## Configuration

Edit `config.py` to modify:
- API credentials and endpoints
- Model parameters (temperature, max_tokens)
- Retry settings
- Base folder path

## Adding New System Prompts

Add new prompts to `prompts.py` and reference them in your processing logic.

## Module Descriptions

- **config.py**: Centralized configuration management
- **prompts.py**: AI system prompts storage
- **api_client.py**: OpenAI API wrapper with token management
- **file_handler.py**: File operations (read/write/directory traversal)
- **retry_handler.py**: Retry logic with exponential backoff
- **processor.py**: Main workflow orchestration
- **main.py**: Application entry point

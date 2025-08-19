# 🤖 CA-Ben

This repository contains the modular Python application used to systematically evaluate Large Language Models (LLMs) against the **CA-Ben (Chartered Accountancy Benchmark)**. It automates the entire workflow, from sending prompts to the models to processing their responses and extracting the final answers for analysis. 📊

-----

## ✨ Features

  - **🧱 Modular Architecture**: Clean separation of concerns. Each module handles a specific task (API calls, file I/O, retry logic), making the code easy to maintain and extend.
  - **🔄 Robust Retry Logic**: Automatically handles API rate limits and transient network errors using an intelligent exponential backoff strategy. Never lose a request\!
  - **🔑 Dynamic Token Management**: Seamlessly refreshes API tokens upon encountering rate limit errors, ensuring uninterrupted long-running evaluation sessions.
  - **📂 Batch File Processing**: Efficiently processes hundreds of question files organized in subdirectories, perfect for large-scale benchmarks.
  - **📝 Structured Excel Output**: Saves all questions, model responses, and extracted answers into neatly organized `.xlsx` files for easy analysis and verification.
  - **⚙️ Centralized Configuration**: Easily manage API keys, model parameters, and file paths from a single `config.py` file.

-----

## 🚀 How to Run

Get the evaluation pipeline up and running in three simple steps:

1.  **Install Dependencies** 📦

    ```bash
    pip install -r requirements.txt
    ```

2.  **Configure Your API Token** 🔑
    Open `src/config.py` and update the `TOKEN` variable with your API key.

    ```python
    TOKEN = "your_super_secret_api_token_here"
    ```

3.  **Launch the Application** ▶️
    Execute the main script from the root directory.

    ```bash
    python src/main.py
    ```

    The application will begin processing the files and you will see the progress in your console.

-----

## 📁 Project Structure & Module Descriptions

The application is organized logically to ensure clarity and maintainability.

```
src/
├── 📜 main.py          # Main entry point - Kicks off the evaluation process.
├── ⚙️ config.py        # Central hub for all settings (API keys, model params, paths).
├── 🧠 prompts.py       # Stores the system prompts used to guide the AI models.
├── 🌐 api_client.py    # Handles all communication with the AI model APIs.
├── 📄 file_handler.py  # Manages all file operations (reading questions, writing results).
├── ⏳ retry_handler.py # Implements the smart retry logic for failed API calls.
├── 🛠️ processor.py       # The core orchestrator that manages the entire workflow.
└── 📋 requirements.txt # A list of all the Python libraries you need.
```

-----

## 💡 Core Logic

The application's workflow is orchestrated by `processor.py` and follows these steps:

1.  **Initialization**: Loads configuration from `config.py` and system prompts from `prompts.py`.
2.  **File Discovery**: The `file_handler.py` scans the specified base folder for all question files.
3.  **Processing Loop**: For each question:
      * The question content is combined with a system prompt.
      * `api_client.py` sends the request to the target LLM.
      * If the API call fails, `retry_handler.py` takes over, waiting and retrying with exponential backoff.
4.  **Response Handling**: The model's raw text response is received.
5.  **Data Storage**: The question, the model's full response, and other metadata are saved to an Excel file by `file_handler.py`.
6.  **Answer Extraction**: A separate process (as described in our paper) parses the Excel files to extract the final answer choices for accuracy calculation.

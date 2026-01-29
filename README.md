# 🤖 CA-Ben

This repository contains the modular Python application used to systematically evaluate Large Language Models (LLMs) against the **CA-Ben (Chartered Accountancy Benchmark)**. It automates the entire workflow, from sending prompts to the models to processing their responses and extracting the final answers for analysis. 📊

-----
**Paper:** *[Large Language Models Acing Chartered Accountancy](https://link.springer.com/article/10.1007/s42979-025-04497-x)*.<br>
**Colab:** *[Benchmark Loading and Analysis Script](https://drive.google.com/file/d/1pTFCfyfWpc0_RmUuSImaaeR9z5kfmlii/view?usp=sharing)*.<br>
**Benchmark:** 📩 *For access to the benchmark data, kindly email the [corresponding author](mailto:aliabidi4685@gmail.com) and cc the [first author](mailto:jatingupta261001@gmail.com) for reference.* 📩

-----

<img width="1436" height="790" alt="image" src="https://github.com/user-attachments/assets/d1b91686-ef44-4824-9819-b6511faade65" />

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
├── 📜 main.py              # Main entry point - Kicks off the evaluation process.
├── ⚙️ config.py            # Central hub for all settings (API keys, model params, paths).
├── 🧠 prompts.py           # Stores the system prompts used to guide the AI models.
├── 🌐 api_client.py        # Handles all communication with the AI model APIs.
├── 📄 file_handler.py      # Manages all file operations (reading questions, writing results).
├── ⏳ retry_handler.py     # Implements the smart retry logic for failed API calls.
├── 🛠️ processor.py         # The core orchestrator that manages the entire workflow.
└── 📋 requirements.txt     # A list of all the Python libraries you need.
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

----

#### 📩 _For access to the benchmark data, kindly email the [corresponding author](mailto:aliabidi4685@gmail.com) and cc the [first author](jatingupta261001@gmail.com) for reference._ 📩
----

### Table: Models' Performance on Foundation, Intermediate, and Final-level Subjects

<table border="1" cellspacing="0" cellpadding="4">
  <thead>
    <tr>
      <th rowspan="2">Models</th>
      <th colspan="2">Foundation</th>
      <th colspan="6">Intermediate</th>
      <th colspan="6">Final</th>
    </tr>
    <tr>
      <th>F1</th><th>F2</th>
      <th>I1</th><th>I2</th><th>I3</th><th>I4</th><th>I5</th><th>I6</th>
      <th>FI1</th><th>FI2</th><th>FI3</th><th>FI4</th><th>FI5</th><th>FI6</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>GPT 4o</td>
      <td>50.00</td><td>58.00</td>
      <td>46.66</td><td>73.33</td><td>20.00</td><td>20.00</td><td>86.66</td><td>75.00</td>
      <td>71.43</td><td>53.33</td><td>78.57</td><td>53.33</td><td>33.33</td><td>41.67</td>
    </tr>
    <tr>
      <td>LLAMA 3.3 70B Int.</td>
      <td>59.00</td><td>56.00</td>
      <td>33.33</td><td>60.00</td><td>40.00</td><td>40.00</td><td>73.33</td><td>75.00</td>
      <td>64.29</td><td>33.33</td><td>71.43</td><td>53.33</td><td>6.67</td><td>20.83</td>
    </tr>
    <tr>
      <td>LLAMA 3.1 405B Int.</td>
      <td>53.00</td><td>59.00</td>
      <td>40.00</td><td>53.33</td><td>20.00</td><td>40.00</td><td>86.66</td><td>56.25</td>
      <td>64.29</td><td>46.67</td><td>71.43</td><td>13.33</td><td>26.67</td><td>41.67</td>
    </tr>
    <tr>
      <td>MISTRAL Large</td>
      <td>41.00</td><td>56.00</td>
      <td>41.66</td><td>53.33</td><td>31.25</td><td>20.00</td><td>73.33</td><td>60.00</td>
      <td>42.86</td><td>41.67</td><td>57.14</td><td>46.67</td><td>13.33</td><td>29.17</td>
    </tr>
    <tr>
      <td>Claude 3.5 Sonnet</td>
      <td>60.00</td><td>60.00</td>
      <td>33.33</td><td>60.00</td><td>20.00</td><td>46.66</td><td>93.33</td><td>75.00</td>
      <td>78.57</td><td>46.67</td><td>64.29</td><td>53.33</td><td>20.00</td><td>62.50</td>
    </tr>
    <tr>
      <td>Microsoft Phi 4</td>
      <td>56.00</td><td>62.00</td>
      <td>46.66</td><td>46.66</td><td>33.33</td><td>33.33</td><td>66.66</td><td>68.75</td>
      <td>64.29</td><td>53.33</td><td>57.14</td><td>26.67</td><td>6.67</td><td>41.67</td>
    </tr>
  </tbody>
</table>



<p><strong>Legend:</strong></p>
<table style="width:100%; border-collapse:collapse;">
  <tr>
    <td style="vertical-align:top; width:50%;">
      <ul>
        <li><strong>F1:</strong> Business Math & Stats</li>
        <li><strong>F2:</strong> Business Econ & BCK</li>
        <li><strong>I1:</strong> Adv. Accounting</li>
        <li><strong>I2:</strong> Corp. Laws</li>
        <li><strong>I3:</strong> Taxation</li>
        <li><strong>I4:</strong> Cost & Mgmt. Acct.</li>
        <li><strong>I5:</strong> Auditing & Ethics</li>
      </ul>
    </td>
    <td style="vertical-align:top; width:50%;">
      <ul>
        <li><strong>I6:</strong> Fin. & Strat. Mgmt.</li>
        <li><strong>FI1:</strong> Fin. Reporting</li>
        <li><strong>FI2:</strong> Adv. Fin. Mgmt.</li>
        <li><strong>FI3:</strong> Adv. Auditing</li>
        <li><strong>FI4:</strong> Direct Tax Laws</li>
        <li><strong>FI5:</strong> Indirect Tax Laws</li>
        <li><strong>FI6:</strong> Integrated Business Sol.</li>
      </ul>
    </td>
  </tr>
</table>

----

## 📚 Citation
If you intend to use this work, please cite as:

```bibtex
@article{Gupta2025,
  author    = {Jatin Gupta and Akhil Sharma and Saransh Singhania and Mohammad Adnan and Sakshi Deo and Ali Imam Abidi and Keshav Gupta},
  title     = {Large Language Models Acing Chartered Accountancy},
  journal   = {SN Computer Science},
  volume    = {6},
  number    = {8},
  pages     = {957},
  year      = {2025},
  month     = {November},
  day       = {11},
  issn      = {2661-8907},
  doi       = {10.1007/s42979-025-04497-x},
  url       = {https://doi.org/10.1007/s42979-025-04497-x}
}



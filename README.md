# Code Base QNA

A chatbot application for answering code-related questions from files from user's directory

---

## Table of Contents

- [Code Base QNA](#code-base-qna)
  - [Table of Contents](#table-of-contents)
  - [Installation](#installation)
  - [Usage](#usage)
    - [Using API Endpoints](#using-api-endpoints)
    - [Using `test.py`](#using-testpy)
  - [Endpoints](#endpoints)
  - [Configuration](#configuration)
  - [Dependencies](#dependencies)

---

## Installation

Follow these steps to set up the project:

1. Clone the repository:

   ```shell
   git clone <repository-url>
   ```

2. Navigate to the project directory:

   ```shell
   cd <project-directory>
   ```

3. Install the required dependencies:

   ```shell
   pip install -r requirements.txt
   ```

4. Set up your environment variables. Create a `.env` file in the project directory and add the following:

   ```env
   BARD__Secure_1PSID=<your-secure-psid>
   ```

   Replace `<your-secure-psid>` with the actual secure PSID provided for authentication.

5. Initialize BardCodeBaseQna by running the following command:

   ```shell
   uvicorn app:app --host 0.0.0.0 --port 8000 --reload
   ```

Now, the application is up and running on `http://localhost:8000`.

---

## Usage

You can interact with the chatbot using the provided API endpoints or by running the `test.py` script.

### Using API Endpoints

1. Initialize BardCodeBaseQna:

   Send a POST request to `/initialize-bard-qna` with the `directory_path` parameter to specify the directory containing code documents. For example:

   ```shell
   curl -X POST "http://localhost:8000/initialize-bard-qna?directory_path=/path/to/code/documents"
   ```

   This initializes the chatbot with the code documents from the specified directory.

2. Chat with the Chatbot:

   Send a POST request to `/chat` with the `message` parameter to interact with the chatbot. For example:

   ```shell
   curl -X POST "http://localhost:8000/chat" -H "Content-Type: application/json" -d '{"message": "How do I implement a binary search in Python?"}'
   ```

   The chatbot will respond with answers to your code-related questions.

### Using `test.py`

1. Run the `test.py` script:

   ```shell
   python test.py
   ```

2. Initialize BardCodeBaseQna:

   Enter the directory path when prompted to initialize BardCodeBaseQna.

3. Chat with the Chatbot:

   Enter your questions or messages when prompted. You can exit the chat by typing "exit," "quit," or "bye."

---

## Endpoints

- **POST /initialize-bard-qna**: Initialize BardCodeBaseQna with code documents from a specified directory.
  - Request Body:
    ```json
    {
      "directory_path": "/path/to/code/documents"
    }
    ```
  - Response Body:
    ```json
    {
      "message": "BardCodeBaseQna initialized successfully"
    }
    ```

- **POST /chat**: Interact with the chatbot by sending messages.
  - Request Body:
    ```json
    {
      "message": "How do I implement a binary search in Python?"
    }
    ```
  - Response Body:
    ```json
    {
      "response": "Chatbot: Here is an example of binary search implementation in Python..."
    }
    ```

---

## Configuration

- The main application logic is in `app.py`.
- The chatbot model is implemented in `bard_code_base_qna.py`.
- The language model is accessed via `bard_llm.py`.
- Code splitting functionality is provided in `code_splitter.py`.
- Example usage of the chatbot is demonstrated in `test.py`.

---

## Dependencies

- [FastAPI](https://fastapi.tiangolo.com/)
- [pydantic](https://pydantic-docs.helpmanual.io/)
- [python-dotenv](https://github.com/theskumar/python-dotenv)
- [langchain](https://github.com/elifesciences/langchain)
- [bardapi](https://github.com/bardcodedev/bardapi)

---

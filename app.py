import os
from dotenv import load_dotenv
from fastapi import FastAPI, Query
from bard_code_base_qna import BardCodeBaseQna
from pydantic import BaseModel

class ChatMessage(BaseModel):
    message: str

# Load environment variables
load_dotenv()
secure_psid = os.getenv("BARD__Secure_1PSID")

if secure_psid is None:
    print("Error: BARD__Secure_1PSID environment variable is not set")
    exit(1)

# Initialize the FastAPI app
app = FastAPI()

# Initialize BardCodeBaseQna
bard_qna = None

@app.post("/initialize-bard-qna")
async def initialize_bard_qna_endpoint(directory_path: str = Query(..., description="Directory path")):
    global bard_qna
    bard_qna = BardCodeBaseQna(secure_psid, directory_path)
    return {"message": "BardCodeBaseQna initialized successfully"}

@app.post("/chat")
async def chat_endpoint(chat_message: ChatMessage):
    message = chat_message.message
    if message.lower() in ["exit", "quit", "bye"]:
        return {"response": "Chatbot: Goodbye!"}
    elif bard_qna:
        response = bard_qna(message)
        return {"response": f"Chatbot: {response}"}
    else:
        return {"response": "Chatbot: BardCodeBaseQna not initialized. Please use the /initialize-bard-qna endpoint."}
    
# Main function to start the application
def main():
    print("Chatbot: Hello! I'm here to help you with your code-related questions.")
    uvicorn.run(app, host="0.0.0.0", port=8000)

if __name__ == "__main__":
    main()

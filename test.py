import requests

initialize_url = "http://localhost:8000/initialize-bard-qna"

# Function to send a message to the chatbot
def send_message(message):
    url = 'http://localhost:8000/chat'

    headers = {
        'accept': 'application/json',
        'Content-Type': 'application/json'
    }

    data = {
        'message': message
    }

    try:
        response = requests.post(url, headers=headers, json=data)

        if response.status_code == 200:
            return response.json()["response"]
        else:
            print(f"Failed to send message. Status code: {response.status_code}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

# Function to initialize BardCodeBaseQna
def initialize_bard_qna(directory_path):
    url = f'http://localhost:8000/initialize-bard-qna?directory_path={directory_path}'  # Replace with the actual URL

    headers = {
        'accept': 'application/json',
    }

    try:
        response = requests.post(url, headers=headers)

        if response.status_code == 200:
            print("BardCodeBaseQna initialized successfully")
            return response.json()
        else:
            print(f"Failed to initialize BardCodeBaseQna. Status code: {response.status_code}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")    

if __name__ == "__main__":
    try:
        print("Initializing BardCodeBaseQna...")
        directory_path = input("Enter the directory path: ")
        initialize_bard_qna(directory_path)

        print("Chatbot: Hello! I'm here to help you with your code-related questions.")

        while True:
            user_input = input("User: ")
            res = send_message(user_input)
            print(res)
            if user_input.lower() in ["exit", "quit", "bye"]:
                break

    except KeyboardInterrupt:
        pass

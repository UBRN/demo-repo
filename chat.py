

def send_user_input(session_id: str, user_input: str) -> str:
    response: requests.Response = requests.post(chatbot_url, json={
        "session_id": session_id,
        "user_input": user_input
    })

    try:
        response_json: Dict[str, str] = json.loads(response.text)
    except json.JSONDecodeError:
        return "Error: Could not decode response from server"

    if "response" not in response_json:
        return "Error: Server response did not contain response field"

    return response_json["response"]

def get_new_session_id() -> str:
    return requests.post(chatbot_url + "/new_session").text

def main():
    session_id: str = get_new_session_id()

    while True:
        user_input: str = input("Enter your message: ")

        response: str = send_user_input(session_id, user_input)
        print(response)

if __name__ == "__main__":


    main()
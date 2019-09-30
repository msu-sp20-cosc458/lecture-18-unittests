def get_chatbot_response(message):
    if message[:2] == "!!":
        return "WooHoo!"
    else:
        return "Invalid command"

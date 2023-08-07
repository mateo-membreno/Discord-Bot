def handle_message(message):
    p_message = message.lower()

    if p_message[0] != "!":
        return
    
    else:
        return "function worked!"
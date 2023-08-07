def handle_response(message) -> str:
    p_message = message.lower()

    if p_message == 'hello':
        return 'Hi!'
    elif p_message == 'roll':
        return str(4)
    else:
        return "function worked!"
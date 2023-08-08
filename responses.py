import openai
import random
import ai_response

def handle_response(message) -> str:
    message = message.lower()
    
    if message.startswith("ai "):
        return ai_response.openai_respond(message[2:])
    elif message == 'roll':
        return int(random() * 6) + 1
    elif message == 'jynxi':
        return "cardiac sensor deployed"
    else:
        return "no reply"
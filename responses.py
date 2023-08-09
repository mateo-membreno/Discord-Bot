import discord
import ai_response
from pathlib import Path

def handle_gpt(message):
    return ai_response.gpt_respond(message)
def handle_dalle(message):
    return ai_response.dalle_respond(message)
def handle_jynxi(message):
    return "cardiac sensor deployed"
def handle_image(message):
    file = discord.File(Path('images/{}.jpeg'.format(message)))
    embed = discord.Embed()
    embed.set_image(url="attachment://{}.jpeg".format(message))
    return file, embed


response_dictionary = {
    "gpt ": handle_gpt,
    "image " : handle_dalle,
    "jynxi " : handle_jynxi,
    "future " : handle_image,
}
def handle_response(message) :
    message = message.lower()
    # splits message into command, rest of message
    parts = message.split(' ', 1)
    command = response_dictionary.get(parts[0]+ ' ')

    if command is None:
        return "no reply"
    # argument is rest of message if exists, if not argument is initial command
    else:
        return command(parts[1]) if len(parts) > 1 else command(parts[0])
    

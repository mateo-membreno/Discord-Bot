import discord
import responses
import os
from dotenv import load_dotenv

async def send_message(message, user_message):
    try:
        response = responses.handle_response(user_message)
        # tuple for image
        if isinstance(response, tuple):
            await message.channel.send(file=response[0], embed=response[1])
        # else for text
        else:
            await message.channel.send(response)
    except Exception as e:
        print(e, "message could not send")

def run_discord_bot():
    load_dotenv()
    TOKEN = os.getenv("TOKEN")

    # set intents for discord
    intents = discord.Intents.default()
    intents.members = True
    intents.messages = True
    intents.message_content = True
    client = discord.Client(intents=intents) 

    # checks bot is running
    @client.event
    async def on_ready():
        print(f'{client.user} is running!')

    # on every message this runs
    @client.event
    async def on_message(message):
        if message.author == client.user:
            return
        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)

        print(username, " said: " ,user_message, " in", channel)
        # checks if message starts with ! so bot responds
        if user_message[0] == '!':
            user_message = user_message[1:]
            await send_message(message, user_message)
        
    client.run(TOKEN)

import discord
import responses
import os
from dotenv import load_dotenv

async def send_message(message, user_message, is_private):
    try:
        response = responses.handle_response(user_message)
        await message.channel.send(response)
    except Exception as e:
        print(e)

def run_discord_bot():
    load_dotenv()
    TOKEN = os.getenv("TOKEN")

    intents = discord.Intents.default()
    intents.members = True
    intents.messages = True
    client = discord.Client(intents=intents) 

    @client.event
    async def on_ready():
        print(f'{client.user} is running!')

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return
        print(message)
        username = str(message.author)
# message content is not working!!!!!
        user_message = str(message.content)
        channel = str(message.channel)

        print(username, " said: _" , user_message, "_ in ", channel)
        await send_message(message, user_message, is_private=False)
        if user_message and user_message[0] == '!':
            user_message = user_message[1:]
            await send_message(message, user_message, is_private=False)
        
        
    client.run(TOKEN)

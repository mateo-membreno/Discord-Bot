import discord
import responses
import os
from dotenv import load_dotenv

async def send_message(message, user_message):
    try:
        response = responses.handle_message(user_message)
        await message.channel.send(response)
    except Exception as e:
        print(e)

def run_discord_bot():
    load_dotenv()
    TOKEN = os.getenv("TOKEN")
    client = discord.Client()

    @client.event
    async def on_ready():
        print(f'{client.user} is running!')

    client.run(TOKEN)
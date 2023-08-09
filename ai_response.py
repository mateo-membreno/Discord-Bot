import openai
import os
from dotenv import load_dotenv
import discord
import requests
from pathlib import Path

load_dotenv()
openai.api_key = os.getenv("OPENAI_KEY")

def gpt_respond(prompt):
    try:
        completions =  openai.Completion.create(
            engine="text-ada-001",
            prompt=prompt,
            max_tokens = 1024,
            n=1,
            stop=None,
            temperature=0.5,
        )
    
        message = completions.choices[0].text
        return message
    except Exception as e:
        print(e, "gpt api failed")
        return("gpt failed")

def dalle_respond(prompt):
    try:
        response = openai.Image.create(
            prompt = prompt,
            n = 1,
            size = "256x256"
        )
        image_url = response['data'][0]['url']
        image = requests.get(image_url).content

        image_path = 'images/{}.jpeg'.format(prompt)
        with open(image_path, 'wb') as f:
            f.write(image)
        file = discord.File(Path(image_path))

        embed = discord.Embed()
        embed.set_image(url="attachment://{}.jpeg".format(prompt))
    
        return file, embed
    except Exception as e:
        print(e, "DALLE api failed")
        return("image failed")
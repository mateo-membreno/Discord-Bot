# Discord Bot
[Click to add **Teo's**  **Bot** to server](https://discord.com/api/oauth2/authorize?client_id=1138187724931735685&permissions=41766446693952&scope=bot)

## Summary of .py files:

- main.py - Runs the Discord bot.

- bot.py - Contains a Discord bot that listens for messages, checks if they start with "!", calls response handling functions, and sends back the bot's response.

- responses.py - Contains response handling functions like calling AI functions from ai_response.py. Handles routing messages to the correct response function based on the command.

- ai_response.py - Contains functions to call the OpenAI APIs for GPT-3 text generation and DALL-E image generation.

## Commands
To access bot begin messages with !

Cmmands:
- gpt --> accesses chat GPT through API call and send text response in channel
    * ex. !gpt what is the population of Orlando, Florida
- image --> accesses OpenAI's DALL·E through API call and send image in channel
    * ex. !image anakin skywalker from star wars
- future --> returns picture of Future 
    * ex. !future





import openai
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_KEY")

def openai_respond(prompt):
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
        print(e, "api failed")
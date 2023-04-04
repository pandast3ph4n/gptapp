import openai 
from dotenv import load_dotenv
import os
import json
import typer
from rich import print


load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
openai.api_key = OPENAI_API_KEY



# Define a function that takes a prompt as input and returns the API response as JSON
def generate_response(prompt):
    # Set the OpenAI API parameters
    model_engine = "davinci"
    prompt_length = 100
    temperature = 0.5

    # Generate a response using the OpenAI API
    response = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=prompt_length,
        temperature=temperature
    )

    print('------------------------------')
    print(response)
    print('------------------------------')

    # Convert the API response to JSON and return it
    return response.choices[0].get("text")

def main(prompt: str):
    response = generate_response(prompt)
    print(response)

if __name__ == "__main__":
    typer.run(main)
    
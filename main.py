import os

from dotenv import load_dotenv
from openai import OpenAI


def main():
    print("Hello from code-agent!")

    #Load API Key
    load_dotenv()
    api_key = os.environ.get("OPENROUTER_API_KEY")
    if api_key is None:
        raise RuntimeError("No API Key found")

    #Create a Client pointing at OpenRouter rather than OpenAI
    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=api_key,
    )

    #Get a response from the model
    response = client.chat.completions.create(
        model='openrouter/free',
        messages=[
            {
                'role': 'user',
                'content': 'Why is Boot.dev such a great place to learn backend development? Use one paragraph maximum.'
            }
        ]
    )
    print(response.choices[0].message.content)

if __name__ == "__main__":
    main()

import argparse
import os

from dotenv import load_dotenv
from openai import OpenAI
from openai.types.chat import ChatCompletionMessageParam


def main() -> None:
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

    #Argparse CLI imput
    parser = argparse.ArgumentParser(description='Chatbot')
    parser.add_argument('user_prompt', type=str, help='User prompt')
    parser.add_argument('--verbose', action='store_true', help='Enable verbose output')
    args = parser.parse_args()

    #Prompt the model
    messages: list[ChatCompletionMessageParam] =[
        {'role': 'user', 'content': args.user_prompt}
    ]
    if args.verbose:
        print(f'User prompt: {args.user_prompt}')

    generate_content(client, messages, args.verbose)

def generate_content(client: OpenAI, messages: list, verbose: bool) -> None:
    response =  client.chat.completions.create(
        model='openrouter/free',
        messages=messages,
    )
    if response.usage is None:
        raise RuntimeError('Failed API request, likely out of usage')

    #Print Response to Terminal
    if verbose:
        print(f'Prompt tokens: {response.usage.prompt_tokens}')
        print(f'Response tokens: {response.usage.completion_tokens}')
    print('Response:')
    print(response.choices[0].message.content)

if __name__ == "__main__":
    main()

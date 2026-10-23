import argparse
import os
import sys

from config import MAX_ITERS
from dotenv import load_dotenv
from openai import OpenAI
from openai.types.chat import ChatCompletion, ChatCompletionMessageParam

from call_functions import available_functions, call_function
from prompts import system_prompt


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
        {'role': 'system', 'content': system_prompt},
        {'role': 'user', 'content': args.user_prompt}
    ]
    if args.verbose:
        print(f'User prompt: {args.user_prompt}')

    #Agent Loop
    for iteration in range(MAX_ITERS):
        try:
            output = generate_content(client, messages, args.verbose)
            if output:
                print('Final Response:')
                print(output)
                return
        except Exception as e:
            print(f"Error in generate_content: {e}")

    print(f'Error: {MAX_ITERS=} reached')
    sys.exit(1)

def generate_content(client: OpenAI, messages: list, verbose: bool) -> str | None:
    response =  client.chat.completions.create(
        model='openrouter/free',
        messages=messages,
        tools=available_functions,
    )
    if response.usage is None:
        raise RuntimeError('Failed API request, likely out of usage')

    #Print Response to Terminal
    if verbose:
        print(f'Prompt tokens: {response.usage.prompt_tokens}')
        print(f'Response tokens: {response.usage.completion_tokens}')
    message = response.choices[0].message
    messages.append(message)
    if not message.tool_calls:
        return message.content

    for tool_call in message.tool_calls:
        if tool_call.type != 'function':
            continue
        result_message = call_function(tool_call, verbose)
        if not result_message['content']:
            raise RuntimeError(f"Empty function response for {tool_call.function.name}")
        if verbose:
            print(f"-> {result_message['content']}")
        messages.append(result_message)

    return None


if __name__ == "__main__":
    main()

import openai
import random

# Set your OpenAI API key
openai.api_key = 'YOUR_OPENAI_API_KEY'

def generate_web3_username(prompt, num_suggestions=5):
    """
    Generates Web3/Crypto themed usernames using OpenAI's GPT model.
    """
    try:
        response = openai.Completion.create(
            model="text-davinci-003",  # You can choose a different model if needed
            prompt=prompt,
            max_tokens=50,
            n=num_suggestions
        )
        suggestions = [resp['text'].strip() for resp in response['choices']]
        return suggestions
    except Exception as e:
        print(f"Error: {e}")
        return []

# Example usage
prompt = "Generate creative and unique usernames related to crypto and Web3."
usernames = generate_web3_username(prompt)

for i, username in enumerate(usernames, 1):
    print(f"Username {i}: {username}")

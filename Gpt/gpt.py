import openai
from dotenv import load_dotenv
import os

# Load the .env file
load_dotenv()

def analyze_html_with_gpt(prompt, html, css, js, api_key):
    """
    This function takes HTML content and sends it to OpenAI's GPT-4 Turbo model for analysis using the new OpenAI API interface.
    It returns the model's response.

    :param html: A string containing HTML content.
    :param api_key: Your OpenAI API key.
    :return: A string containing the GPT-4 Turbo model's response.
    """
    openai.api_key = api_key

    prompt = f"{prompt}"

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4-1106-preview",  # Specify model
            messages=[{"role": "system", "content": "You are a helpful assistant."}, 
                {"role": "user", "content": prompt}],
            max_tokens=150  # Adjust the number of tokens as needed
        )
        return response['choices'][0]['message']['content']
    except Exception as e:
        print(f"An error occurred: {e}")
        return None


#create main function
def get_response(prompt):
    api_key = os.getenv("OPENAI_API_KEY")
    response = analyze_html_with_gpt(prompt, api_key)
    return response




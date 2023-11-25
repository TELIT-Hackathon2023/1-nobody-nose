import openai
from dotenv import load_dotenv
import os

# Load the .env file
load_dotenv()

def analyze_html_with_gpt(prompt, api_key):
    """
    This function takes HTML content and sends it to OpenAI's GPT-4 Turbo model for analysis using the new OpenAI API interface.
    It returns the model's response.

    :param prompt: A string containing HTML content.
    :param api_key: Your OpenAI API key.
    :return: A string containing the GPT-4 Turbo model's response.
    """
    openai.api_key = api_key

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4-1106-preview",
            messages=[{"role": "system", "content": "You are an assistant skilled in analyzing and providing feedback on Webiste content. HTML CSS AND JS are the three main components of a website. You are given a website's HTML, CSS and JS files. You need to rate the website based on the given"},
                        {"role": "user", "content": prompt}],
            max_tokens=4095,
            temperature=0.4,
            top_p=0.8,
            frequency_penalty=0.5,
            presence_penalty=0.2,
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




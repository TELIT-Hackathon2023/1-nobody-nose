import openai
from dotenv import load_dotenv
import os
import requests

# Load the .env file
load_dotenv()

def scrape_html(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # This will raise an HTTPError if the HTTP request returned an unsuccessful status code.
        return response.text
    except requests.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except Exception as err:
        print(f"An error occurred: {err}")

def analyze_html_with_gpt(prompt, html, api_key):
    """
    This function takes HTML content and sends it to OpenAI's GPT-4 Turbo model for analysis using the new OpenAI API interface.
    It returns the model's response.

    :param html: A string containing HTML content.
    :param api_key: Your OpenAI API key.
    :return: A string containing the GPT-4 Turbo model's response.
    """
    openai.api_key = api_key

    prompt = f"{prompt}:\nHTML file you work with\n{html}"

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
def get_response(prompt, url):
    api_key = os.getenv("OPENAI_API_KEY")
    html_content = scrape_html(url)
    response = analyze_html_with_gpt(prompt, html_content, api_key)
    print(response)




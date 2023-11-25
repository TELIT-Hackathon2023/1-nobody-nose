import requests
from openai import OpenAI

api_key = "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"
client = OpenAI(api_key=api_key)

def scrape_html(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # This will raise an HTTPError if the HTTP request returned an unsuccessful status code.
        return response.text
    except requests.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except Exception as err:
        print(f"An error occurred: {err}")


def analyze_html_with_gpt(html, api_key):
    """
    This function takes HTML content and sends it to OpenAI's GPT-4 Turbo model for analysis.
    It returns the model's response.

    :param html: A string containing HTML content.
    :param api_key: Your OpenAI API key.
    :return: A string containing the GPT-4 Turbo model's response.
    """
    

    prompt = f"Analyze the following HTML code and provide insights:\n\n{html}"

    try:
        response = openai.Completion.create(
            model="gpt-4-turbo",  # Specify GPT-4 Turbo model
            prompt=prompt,
            max_tokens=150,  # Adjust the number of tokens as needed
            n=1,  # Number of completions to generate
            stop=None,  # Specify any stopping criteria if needed
            temperature=0.5  # Adjust the temperature if you want more creative responses
        )
        return response['choices'][0]['text'].strip()
    except Exception as e:
        print(f"An error occurred: {e}")
        return None




#create a main function
def main():
    #get the url
    url = "https://telekom.sk/"  # Replace with your desired URL
    feedback = get_gpt_feedback(scrape_html(url))
    print(feedback)


#call the main function
if __name__ == "__main__":
    main()
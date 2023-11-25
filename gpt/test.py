#execute main function
from gpt import get_response

url = "https://telekom.sk"

if __name__ == "__main__":
    get_response("What is the title of the page?", url)
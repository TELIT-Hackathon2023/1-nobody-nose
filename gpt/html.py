import requests

def scrape_html(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # This will raise an HTTPError if the HTTP request returned an unsuccessful status code.
        return response.text
    except requests.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except Exception as err:
        print(f"An error occurred: {err}")

# Example URL
url = "https://telekom.sk/"  # Replace with your desired URL

# Scrape and print HTML
html_content = scrape_html(url)
if html_content:
    print(html_content)

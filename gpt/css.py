import requests
from bs4 import BeautifulSoup
import os

def print_css(url):
    try:
        # Send a request to the URL
        response = requests.get(url)
        response.raise_for_status()

        # Parse the content with BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find all links to CSS files
        css_links = soup.find_all('link', rel='stylesheet')

        for i, link in enumerate(css_links):
            href = link['href']
            if not href.startswith('http'):
                href = os.path.join(url, href)

            # Fetch each CSS file
            css_response = requests.get(href)
            css_response.raise_for_status()

            # Print CSS content
            print(f'CSS File {i+1} Content:\n{css_response.text}\n')

        print(f'Total {len(css_links)} CSS files found.')

    except requests.RequestException as e:
        print(f'An error occurred: {e}')

# Example usage
print_css('https://www.telekom.sk')

"""
Script for downloading JavaScript libraries referenced in the HTML of a given URL.

Usage:
    - Define the function `download_js_libraries(url, save_directory)` to retrieve the HTML content
      from the specified URL, parse it using BeautifulSoup to find all script tags with a 'src' attribute,
      download each JavaScript library referenced by these tags, and save them to the specified directory.
    - Set the `target_url` variable to specify the URL from which to download JavaScript libraries.
    - Set the `save_directory` variable to specify the directory where the downloaded JavaScript files will be saved.

Requirements:
    - requests library: `pip install requests`
    - BeautifulSoup library: `pip install beautifulsoup4`

Note:
    - This script requires internet connectivity to download JavaScript libraries from remote URLs.
    - It uses requests to make HTTP requests and BeautifulSoup for HTML parsing.
"""

import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

def download_js_libraries(url, save_directory):
    """
    Downloads JavaScript libraries referenced in the HTML of a given URL.

    Args:
        url (str): The URL of the webpage where JavaScript libraries are referenced.
        save_directory (str): The directory path where downloaded JavaScript files will be saved.
    """
    # Make a request to the target URL
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse HTML content
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find all script tags with a 'src' attribute
        script_tags = soup.find_all('script', {'src': True})

        # Download each JS library
        for script_tag in script_tags:
            js_url = script_tag['src']
            absolute_url = urljoin(url, js_url)

            # Ensure the URL is valid and has a .js extension
            if js_url.endswith('.js'):
                # Get the filename from the URL
                filename = os.path.basename(urlparse(js_url).path)

                # Save the JS file to the specified directory
                save_path = os.path.join(save_directory, filename)

                # Download the JS file
                js_content = requests.get(absolute_url).text
                with open(save_path, 'w', encoding='utf-8') as file:
                    file.write(js_content)

                print(f"Downloaded: {js_url} => {save_path}")

    else:
        print(f"Failed to retrieve content from {url}. Status code: {response.status_code}")

if __name__ == "__main__":
    target_url = "https://example.com"  # Replace with your target URL
    save_directory = "js_libraries"  # Directory to save downloaded JS files

    # Create the save directory if it doesn't exist
    if not os.path.exists(save_directory):
        os.makedirs(save_directory)

    download_js_libraries(target_url, save_directory)

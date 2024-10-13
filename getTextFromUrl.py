import requests
from bs4 import BeautifulSoup

def getTextFromUrl(url):
    # Send a GET request to the webpage
    response = requests.get(url)
    
    # Check if the request was successful
    if response.status_code != 200:
        return f"Failed to retrieve content. Status code: {response.status_code}"

    # Parse the webpage content with BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extract all text from the webpage
    page_text = soup.get_text()

    return page_text

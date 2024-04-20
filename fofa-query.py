import requests
from bs4 import BeautifulSoup
import time

def scrape_page(url, cookie):
    # Set up the cookies
    cookies = {
        'fofa_token': cookie
    }

    # Send a GET request to the URL with the cookies
    try:
        response = requests.get(url, cookies=cookies)
        response.raise_for_status()  # Raise an exception for HTTP errors
    except requests.exceptions.RequestException as e:
        print("Error:", e)
        return None

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find all elements with the key "data-clipboard-text"
        clipboard_elements = soup.find_all(attrs={"data-clipboard-text": True})

        # Extract the values of the elements
        values = sorted([element['data-clipboard-text'] for element in clipboard_elements])

        return values
    else:
        print("Failed to retrieve page:", response.status_code)
        return None

# Base URL
base_url = "insert fofa query url"

# Prompt user for file name to save data
file_name = input("Enter the name of the file to save the data: ")

# Cookie - Create an account on en.fofa.info, login and view cookies (use devtools or cookie editor plugin). copy fofa_token andpaste it here.

#cookie = "fofa_token_jwt_token"
cookie = "insert fofo coockie"

# Iterate over pages from 1 to 3
for page_number in range(1, 4):
    # Construct URL for the current page
    url = base_url + str(page_number) + "&page_size=20"

    # Scrape the page
    print(f"Global Protect {page_number}:")
    data_values = scrape_page(url, cookie)
    if data_values:
        # Write data to file
        with open(f"{file_name}_page{page_number}.txt", "w") as f:
            f.write("\n".join(data_values))
        print("Data saved to file.")
        print()  # Add an empty line between pages

    # Add a delay before scraping the next page
    time.sleep(3)  # Adjust the delay time as needed

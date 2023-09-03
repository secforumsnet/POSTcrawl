import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse, urljoin
from colorama import init, Fore
import threading

# Initialize colorama for colored text
init(autoreset=True)

# Function to extract base domain from a URL
def get_base_domain(url):
    parsed_url = urlparse(url)
    return parsed_url.netloc

# Function to crawl a URL and identify forms with POST method
def crawl_url(url, visited_urls, max_depth, post_forms_file):
    try:
        print(f"Crawling URL: {url}")  # Print the current URL being crawled

        # Send an HTTP GET request to the URL
        response = requests.get(url)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the HTML content with BeautifulSoup to find forms
            soup = BeautifulSoup(response.text, 'html.parser')
            forms = soup.find_all('form')

            # Add the URL to the set of visited URLs to avoid revisiting
            visited_urls.add(url)

            # Check for forms using the POST method
            for form in forms:
                if form.get('method', '').lower() == 'post':
                    print(Fore.GREEN + f"Form with POST method found at: {url}" + Fore.RESET)
                    with open(post_forms_file, 'a') as file:
                        file.write(f"{url}\n")

            # Follow links to other pages and domains
            for link in soup.find_all('a', href=True):
                href = link['href']

                # Ensure the link is not already visited
                absolute_url = urljoin(url, href)
                if absolute_url not in visited_urls and max_depth > 0:
                    crawl_url(absolute_url, visited_urls, max_depth - 1, post_forms_file)

        else:
            print(f"Failed to retrieve {url}. Status code: {response.status_code}")

    except requests.exceptions.RequestException as e:
        print(f"An error occurred while fetching the page: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Input the filename containing starting URLs
file_name = input("Enter the filename containing starting URLs: ")

# Create a set to store visited URLs
visited_urls = set()

# Set the maximum depth for crawling (unlimited in this case)
max_depth = float("inf")

# Create a file to store URLs with forms using POST method
post_forms_file = "urls_with_post_forms.txt"
open(post_forms_file, 'w').close()  # Clear the file if it exists

# Read starting URLs from the input file
try:
    with open(file_name, 'r') as file:
        starting_urls = [line.strip() for line in file]

    # Create a thread for each starting URL
    threads = []
    for starting_url in starting_urls:
        thread = threading.Thread(target=crawl_url, args=(starting_url, visited_urls, max_depth, post_forms_file))
        threads.append(thread)
        thread.start()

    # Wait for all threads to finish
    for thread in threads:
        thread.join()

except FileNotFoundError:
    print(f"File '{file_name}' not found.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

print("Crawling complete. URLs with forms using POST method are saved in 'urls_with_post_forms.txt'.")

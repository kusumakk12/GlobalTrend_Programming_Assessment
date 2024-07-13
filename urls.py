import requests
from requests.exceptions import RequestException
import time

def download_urls(urls, max_retries=3, delay=1):
    results = {}

    for url in urls:
        retries = 0
        while retries < max_retries:
            try:
                response = requests.get(url, timeout=10)
                response.raise_for_status()  
                results[url] = response.text
                break  
            except RequestException as e:
                retries += 1
                print(f"Error downloading {url} (attempt {retries}/{max_retries}): {str(e)}")
                if retries == max_retries:
                    results[url] = f"Failed after {max_retries} attempts: {str(e)}"
                else:
                    time.sleep(delay)  
            except Exception as e:
                print(f"Unexpected error for {url}: {str(e)}")
                results[url] = f"Unexpected error: {str(e)}"
                break  

    return results

urls = [
    "https://www.example.com",
    "https://www.python.org",
    "https://www.nonexistent-url-123456.com", 
    "https://api.github.com/users/octocat"
]

results = download_urls(urls)

for url, content in results.items():
    print(f"\nURL: {url}")
    print(f"Content: {content[:100]}...") 

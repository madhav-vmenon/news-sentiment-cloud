import requests #sends HTTP requests
import json #allows read/write of json files

from config import NEWS_API_KEY

def fetch_articles(query="technology", page_size=100):
    url = (
        f"https://newsapi.org/v2/everything?"
        f"q={query}&pageSize={page_size}&apiKey={NEWS_API_KEY}" # query is what you want to search and page_size is how many results
    )

    # Send an HTTP GET request to the API endpoint
    # 'resp' now contains the response object (headers, status code, body)
    resp = requests.get(url)

    # Convert the JSON response body into a Python dictionary
    data = resp.json()

    print("API status:", data.get("status"))


    # ---- Save data locally so you can use it later ----
    # Open a file named 'raw_news.json' in write mode
    with open("raw_news.json", "w") as f:
        # Write the JSON data to the file with pretty indentation
        json.dump(data, f, indent=2)


    return data

# This block runs only if this file is executed directly (not imported)
# Good for testing your function
if __name__ == "__main__":
    fetch_articles()





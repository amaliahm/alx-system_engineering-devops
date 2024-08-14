import requests

def recurse(subreddit, hot_list=[], after=None):
    # Define the base URL for the Reddit API
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    
    # Define the headers to mimic a browser request
    headers = {"User-Agent": "Mozilla/5.0"}

    # Set up the parameters, including the 'after' token for pagination
    params = {"after": after}

    # Make the request to the Reddit API
    response = requests.get(url, headers=headers, params=params, allow_redirects=False)

    # Check if the subreddit is valid (status code 200) and not a redirect
    if response.status_code != 200:
        return None

    # Parse the JSON response
    data = response.json()

    # Extract the list of hot articles
    articles = data.get("data", {}).get("children", [])

    # Add the titles to the hot_list
    hot_list.extend([article["data"]["title"] for article in articles])

    # Check if there is a next page (pagination)
    after = data.get("data", {}).get("after", None)

    # If there's no next page, return the accumulated hot_list
    if after is None:
        return hot_list

    # Recursive call to fetch the next page
    return recurse(subreddit, hot_list, after)

# Example usage
if __name__ == "__main__":
    subreddit = "programming"
    titles = recurse(subreddit)
    if titles:
        print(f"Number of hot articles: {len(titles)}")
        print(titles)
    else:
        print("None")


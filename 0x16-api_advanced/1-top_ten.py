#!/usr/bin/python3
"""Contains top_ten function"""
import requests


def top_ten(subreddit):
    """Prints the titles of the first 10 hot posts for a given subreddit."""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "Mozilla/5.0"}
    params = {"limit": 10}

    response = requests.get(url, headers=headers, params=params, allow_redirects=False)

    if response.status_code != 200:
        print(None)
        return

    data = response.json()
    posts = data.get("data", {}).get("children", [])

    if not posts:
        print(None)
        return

    for post in posts:
        print(post["data"]["title"])


if __name__ == "__main__":
    top_ten("programming")


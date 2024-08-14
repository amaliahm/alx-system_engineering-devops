#!/usr/bin/python3
"""Contains recurse function"""
import requests


def recurse(subreddit, hot_list=None, after=None):
    """Recursively queries the Reddit API and returns a list of titles of hot articles."""
    if hot_list is None:
        hot_list = []

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "Mozilla/5.0"}
    params = {"after": after}

    response = requests.get(url, headers=headers, params=params, allow_redirects=False)

    if response.status_code != 200:
        return None

    data = response.json()
    articles = data.get("data", {}).get("children", [])
    hot_list.extend([article["data"]["title"] for article in articles])

    after = data.get("data", {}).get("after", None)

    if after is None:
        return hot_list

    return recurse(subreddit, hot_list, after)


if __name__ == "__main__":
    subreddit = "programming"
    titles = recurse(subreddit)
    if titles:
        print(f"Number of hot articles: {len(titles)}")
        print(titles)
    else:
        print("None")



#!/usr/bin/python3
"""
Contains the number_of_subscribers function
"""

import requests


def number_of_subscribers(subreddit):
    """returns the number of subscribers for a given subreddit"""
     url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "Mozilla/5.0"}

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        return 0

    data = response.json()
    subscribers = data.get("data", {}).get("subscribers", 0)
    return subscribers


if __name__ == "__main__":
    subreddit = "programming"
    print(f"Subscribers: {number_of_subscribers(subreddit)}")

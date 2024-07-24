#!/usr/bin/python3
"""
Module to fetch and print the titles of the first 10 hot posts
from a given subreddit using the Reddit API.
"""

import requests


def top_ten(subreddit):
    """
    Queries the Reddit API and prints the titles of the first
    10 hot posts for a given subreddit.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'my-reddit-app'}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json().get('data', {}).get('children', [])
        for post in data[:10]:
            print(post['data']['title'])
    else:
        print(None)

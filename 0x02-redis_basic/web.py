#!/usr/bin/env python3
"""Module containing function to return HTML content of a particular url"""
import redis
import requests


def get_page(url: str) -> str:
    """Function that returns HTML content of a URL"""

    data = redis.Redis()
    count = 0

    data.set(f"cached:{url}", count)
    content = requests.get(url)
    data.incr(f"count:{url}")
    data.setex(f"cached:{url}", 10, data.get(f"cached:{url}"))
    return content.text


if __name__ == "__main":
    get_page('http://slowwly.robertomurray.co.uk')

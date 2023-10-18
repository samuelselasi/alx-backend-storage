#!/usr/bin/env python3
"""Module containing function to return HTML content of a particular url"""
import redis
import requests

data = redis.Redis()


def get_page(url: str) -> str:
    """Function that returns HTML content of a URL"""

    cached_content = data.get(f"cached:{url}")
    if cached_content:
        return cached_content.decode('utf-8')

    count = data.incr(f"count:{url}")
    content = requests.get(url).text

    data.setex(f"cached:{url}", 10, content)
    return content


# if __name__ == "__main__":
    # content = get_page('http://slowwly.robertomurray.co.uk')
    # print(content)

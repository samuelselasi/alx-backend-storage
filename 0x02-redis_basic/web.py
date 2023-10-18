#!/usr/bin/env python3
"""Module containing function to return HTML content of a particular url"""
import redis
import requests
# from functools import wraps

# Create a Redis client instance
data = redis.Redis()
count = 0

'''
def url_count(method):
    """Function that returns the number of times a URL was accessed with key"""

    def wrapper(url):
        """Function that defines the wrapper"""

        key = "cached:" + url
        value = data.get(key)
        if value:
            return value.decode("utf-8")

        count = "count:" + url
        content = method(url)

        data.incr(count)
        data.set(key, content, ex=10)
        data.expire(key, 10)
        return content
    return wrapper
'''


# @url_count  # Decorate get_page with url_count function
def get_page(url: str) -> str:
    """Function that returns HTML content of a URL"""

    data.set(f"cached:{url}", count)
    content = requests.get(url)
    data.incr(f"count:{url}")
    data.setex(f"cached:{url}", 10, r.get(f"cached:{url}"))
    return content.text


if __name__ == "__main":
    get_page('http://slowwly.robertomurray.co.uk')

#!/usr/bin/env python3
"""Module containing function to return HTML content of a particular url"""
import redis
import requests
from functools import wraps
from typing import Callable

data = redis.Redis()


def call_history(method: Callable) -> Callable:
    """Function to store the history of inputs and outputs of a function"""

    key = method.__qualname__
    inputs = key + ":inputs"
    outputs = key + ":outputs"

    @wraps(method)
    def wrapper(url: str):
        """Function that defines wrapper"""

        data.rpush(inputs, url)
        cached_content = data.get(f"cached:{url}")
        if cached_content:
            data.rpush(outputs, cached_content.decode('utf-8'))
            return cached_content.decode('utf-8')

        content = method(url)
        data.rpush(outputs, content)
        return content
    return wrapper


def count_calls(method: Callable) -> Callable:
    """Function to count the number of times a function is called"""

    key = method.__qualname__

    @wraps(method)
    def wrapper(url: str):
        """Function that defines wrapper"""

        data.incr(key)
        return method(url)
    return wrapper


@call_history
@count_calls
def get_page(url: str) -> str:
    """Function that returns HTML content of a URL"""

    cached_content = data.get(f"cached:{url}")
    if cached_content:
        return cached_content.decode('utf-8')

    count = data.incr(f"count:{url}")
    content = requests.get(url).text

    data.setex(f"cached:{url}", 10, content)
    return content


if __name__ == "__main__":
    get_page('http://slowwly.robertomurray.co.uk')

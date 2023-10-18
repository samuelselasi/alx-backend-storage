#!/usr/bin/env python3
"""Module handling Redis client for data storage"""
import redis
from uuid import uuid4
from typing import Union
from typing import Optional, Callable
from functools import wraps


# Task 3: Storing lists
def call_history(method: Callable) -> Callable:
    """Function to store the history of inputs and outputs of a function"""

    key = method.__qualname__
    inputs = key + ":inputs"
    outputs = key + ":outputs"

    @wraps(method)
    def wrapper(self, *args, **kwds):
        """Function that defines wrapper"""

        self._redis.rpush(inputs, str(args))
        data = method(self, *args, **kwds)
        self._redis.rpush(outputs, str(data))
        return data
    return wrapper


# Task 2: Incrementing values
def count_calls(method: Callable) -> Callable:
    """Function to count no. of times methods of Cache are called"""

    key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwds):
        """Funtion that defines wrapper"""

        self._redis.incr(key)
        return method(self, *args, **kwds)
    return wrapper


# Task 0: Writing strings to Redis
class Cache:
    """Class that contains methods with Redis instance attributes"""

    def __init__(self):
        """Method that stores and flushes private redis instances"""

        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls  # Decorate Cache.store with count_calls function
    @call_history  # Decorate Cache.store with call_history function
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Method that takes data, generates key to store & returns the key"""

        key = str(uuid4())
        self._redis.set(key, data)
        return key

    # Task 1: Reading from Redis and recovering original type
    def get(self, key: str, fn: Optional[Callable] = None) -> Union[
            str, bytes, int, float]:
        """Method that converts data back to original format"""

        data = self._redis.get(key)
        if fn is not None:
            return fn(data)
        return data

    def get_str(self, key: str) -> str:
        """Method that automatically paramatize class Cache.get to str"""

        data = self._redis.get(key)
        return data.decode("utf-8")

    def get_int(self, key: str) -> int:
        """Method that automatically paramatize class Cache.get to str"""

        data = self._redis.get(key)
        try:
            data = int(value.decode("utf-8"))
        except Exception:
            data = 0
        return data


# Task 4: Retrieving lists
def replay(method: Callable):
    """Function that prints the history of calls of a function"""

    key = method.__qualname__
    inputs = key + ":inputs"
    outputs = key + ":outputs"

    redis = method.__self__._redis
    count = redis.get(key).decode("utf-8")
    print("{} was called {} times:".format(key, count))

    list_input = redis.lrange(inputs, 0, -1)
    list_output = redis.lrange(outputs, 0, -1)
    zipped = list(zip(list_input, list_output))

    for ins, outs in zipped:
        attr, data = ins.decode("utf-8"), outs.decode("utf-8")
        print("{}(*{}) -> {}".format(key, attr, data))

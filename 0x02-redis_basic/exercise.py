#!/usr/bin/env python3
"""Module handling Redis client for data storage"""
import redis
from uuid import uuid4
from typing import Union
from typing import Optional, Callable


class Cache:
    """Class that contains methods with Redis instance attributes"""

    def __init__(self):
        """Method that stores and flushes private redis instances"""

        self._redis = redis.Redis()
        self._redis.flushdb()

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

#!/usr/bin/env python3
"""Module handling Redis client for data storage"""
import redis
from uuid import uuid4
from typing import Union


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

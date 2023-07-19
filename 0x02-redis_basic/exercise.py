#!/usr/bin/env python3
"""Introductionm to redis"""
from typing import Union, Optional, Callable
import redis
from uuid import uuid4
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """Wrapper for counting number of calls"""
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """Wrapper utility method"""
        key = method.__qualname__
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper


class Cache:
    """This class is an implementation of a cache"""

    def __init__(self):
        """Inityializes the class"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Stores a random set of data"""
        key = str(uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable] = None) -> Union[
            str, bytes, int, float]:
        """Retrieves an item from redis"""
        val = self._redis.get(key)
        sol = val
        if val and fn:
            sol = fn(val)
        return sol

    def get_str(self, key: str) -> str:
        """Gets a string"""
        return self.get(key, str)

    def get_int(self, key: str) -> int:
        """Gets an int """
        return self.get(key, int)

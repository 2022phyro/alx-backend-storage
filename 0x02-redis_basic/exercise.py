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


def call_history(method: Callable) -> Callable:
    """Recording call history"""
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """Wrapper utility function"""
        i_key = f"{method.__qualname__}:inputs"
        o_key = f"{method.__qualname__}:outputs"
        self._redis.rpush(i_key, str(args))
        out = method(self, *args, **kwargs)
        self._redis.rpush(o_key, out)
        return out
    return wrapper


def replay(method: Callable) -> None:
    """Replaying last commands"""
    temp = redis.Redis()
    name = method.__qualname__
    i_key = f"{name}:inputs"
    o_key = f"{name}:outputs"
    inn = temp.lrange(i_key, 0, -1)
    out = temp.lrange(o_key, 0, -1)
    count = temp.get(name).decode('utf-8')

    print(f"{name} was called {count} times:")
    for i, j in zip(inn, out):
        i = i.decode('utf-8')
        j = j.decode('utf-8')
        print(f"{name}(*{i}) -> {j}")


class Cache:
    """This class is an implementation of a cache"""

    def __init__(self):
        """Initializes the class"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
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

#!/usr/bin/env python3
"""Introductionm to redis"""
from typing import Any
import redis
from uuid import uuid4


class Cache:
    """This class is an implementation of a cache"""

    def __init__(self):
        """Inityializes the class"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Any) -> str:
        """Stores a random set of data"""
        key = str(uuid4())
        self._redis.set(key, data)
        return key

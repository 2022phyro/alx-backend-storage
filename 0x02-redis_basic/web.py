#!/usr/bin/env python3
"""Caching a website"""
from typing import Callable
import redis
from functools import wraps
import requests


def track(func: Callable) -> Callable:
    """Caches our requests to a url"""
    @wraps(func)
    def wrapper(url):
        """Wrapper utility function"""
        cache = redis.Redis()
        key = f"count:{url}"
        cache.incr(key)
        res = cache.get(url)
        if res:
            return res.decode('utf-8')
        res = func(url)
        cache.setex(url, 10, res)
        return res
    return wrapper


@track
def get_page(url: str) -> str:
    """Carries out a Http request"""
    val = requests.get(url)
    return val.text

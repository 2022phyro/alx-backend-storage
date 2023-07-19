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
        cache = redis.Redis()
        """Wrapper utility function"""
        key = f"count:{url}"
        cache.incr(key)
        res = cache.get(url)
        if res:
            return res
        res = func(url)
        cache.set(url, res)
        cach.expire(url, 10)
        return res
    return wrapper


@track
def get_page(url: str) -> str:
    """Carries out a Http request"""
    val = requests.get(url)
    return val

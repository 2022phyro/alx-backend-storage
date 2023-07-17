#!/usr/bin/env python3
"""Updating with pymongo"""


def update_topics(mongo_collection, name, topics):
    """Update documents according to a given criteria"""
    criteria = {"name": name}
    values = {"$set": {"topics": topics}}
    mongo_collection.update_many(criteria, values)

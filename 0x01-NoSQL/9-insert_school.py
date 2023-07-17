#!/usr/bin/env python3
"""Inserting stuff with pymongo"""


def insert_school(mongo_collection, **kwargs):
    """Inserts a new item"""
    newItem = mongo_collection.insert_one(kwargs)
    return newItem.inserted_id

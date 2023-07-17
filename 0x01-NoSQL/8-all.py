#!/usr/bin/env python3
"""Learning to use mongofb with python"""


def list_all(mongo_collection):
    """Lists all docs in a collection"""
    return mongo_collection.find()

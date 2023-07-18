#!/usr/bin/env python3
"""Checking all schools that have a spexific topic"""


def schools_by_topic(mongo_collection, topic):
    """Checks if a school have a specific topic"""
    schools = mongo_collection.find()
    return [school for school in schools if topic in school.get('topics', [])]

#!/usr/bin/env python3
"""Calcuclates average score for each individual"""


def top_students(mongo_collection):
    """Calculates the average"""
    stud = mongo_collection.find()
    for m in stud:
        l = m.get('title', [])
        score = [x.get("score", 0) for x in l]
        if not score:
            ave = 0
        else:
            ave = sum(score) / len(score)
    mongo_collection.update_many(
            {"$set": {"averageScore":
                
                }}
            )
    return mongo_collection.find().sort("averageScore", -1)

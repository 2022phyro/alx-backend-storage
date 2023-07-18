#!/usr/bin/env python3
"""Calcuclates average score for each individual"""


def top_students(mongo_collection):
    """Calculates the average"""
    pipeline = [
        {
            '$unwind': '$topics'
        },
        {
            '$group': {
                '_id': '$_id',
                'name': {'$first': '$name'},
                'total_score': {'$sum': '$topics.score'},
                'count': {'$sum': 1}
            }
        },
        {
            '$project': {
                '_id': 1,
                'name': 1,
                'averageScore': {'$divide': ['$total_score', '$count']}
            }
        },
        {
            '$sort': {
                'averageScore': -1
            }
        }
    ]
    result = list(mongo_collection.aggregate(pipeline))
    return result

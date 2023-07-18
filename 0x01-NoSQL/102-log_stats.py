#!/usr/bin/env python3
"""Parsing log files"""
from pymongo import MongoClient, DESCENDING

if __name__ == '__main__':
    """Attempts to parse the log files"""
    client = MongoClient('mongodb://127.0.0.1:27017')
    logs = client.logs.nginx
    print(logs.count_documents({}), 'logs')
    options = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print("Methods:")
    for val in options:
        x = logs.count_documents({'method': val})
        print("\tmethod {}: {:d}".format(val, x))
    status = logs.count_documents({'path': '/status', 'method': 'GET'})
    print("{} status check".format(status))
    pipeline = [{
        '$group': {
            '_id': '$ip',
            'count': {'$sum': 1}
            }
        },
        {
            '$sort': {
                'count': DESCENDING}
        },
        {
            '$limit': 10
        }]
    result = list(logs.aggregate(pipeline))
    print("IPs:")
    for doc in result:
        print(f"\t{doc.get('_id')}: {doc.get('count')}")

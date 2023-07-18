#!/usr/bin/env python3
"""Parsing log files"""
from pymongo import MongoClient

if __name__ == '__main__':
    client = MongoClient('mongodb://127.0.0.1:27017')
    logs = client.logs.nginx
    print(logs.count_documents({}), 'logs')
    options = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print("Methods:")
    for val in options:
        x = logs.count_documents({'method': val})
        print("    method {}: {:d}".format(val, x))
    status = logs.count_documents({'path': '/status'})
    print("{} status check".format(status))

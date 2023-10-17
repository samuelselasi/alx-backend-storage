#!/usr/bin/env python3
"""Script that returns Nginx logs stats stored in MongoDB"""
import pymongo


client = pymongo.MongoClient('mongodb://127.0.0.1:27017')
database = client['logs']
collection = database['nginx']

logs = collection.count_documents({})
print(f"{logs} logs")

all_methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
methods = {method: collection.count_documents(
    {"method": method}) for method in all_methods}
print("Methods:")
for method, count in methods.items():
    print(f"    method {method}: {count}")

status = collection.count_documents({"method": "GET", "path": "/status"})
print(f"{status} status check")

client.close()

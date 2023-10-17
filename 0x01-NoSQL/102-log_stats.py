#!/usr/bin/env python3
"""Module containing script that returns Nginx stats stored in MongoDB"""
import pymongo

client = pymongo.MongoClient('mongodb://127.0.0.1:27017')
logs = client.logs.nginx
print("{} logs".format(logs.estimated_document_count()))

print("Methods:")
for method in ["GET", "POST", "PUT", "PATCH", "DELETE"]:
    count = logs.count_documents({'method': method})
    print("\tmethod {}: {}".format(method, count))

status = logs.count_documents({'method': 'GET', 'path': "/status"})
print("{} status check".format(status))
print("IPs:")

topIps = logs.aggregate(
        [{"$group": {"_id": "$ip", "count": {"$sum": 1}}},
            {"$sort": {"count": -1}}, {"$limit": 10},
            {"$project": {"_id": 0, "ip": "$_id", "count": 1}}])
for ip in topIps:
    print("\t{}: {}".format(ip.get('ip'), ip.get('count')))

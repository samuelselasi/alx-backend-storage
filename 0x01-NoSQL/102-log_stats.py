#!/usr/bin/env python3
"""Module containing script that returns Nginx stats stored in MongoDB"""
import pymongo


def collection(db: dict) -> int:
    """Function to retroeve logs information"""
    client = pymongo.MongoClient('mongodb://127.0.0.1:27017')
    logs = client.logs.nginx
    return logs.count_documents(db)


def main():
    """Function that returns stats about Nginx logs stored in MongoDB"""

    print(f"{collection({})} logs")
    print("Methods:")
    print(f"\tmethod GET: {collection({'method': 'GET'})}")
    print(f"\tmethod POST: {collection({'method': 'POST'})}")
    print(f"\tmethod PUT: {collection({'method': 'PUT'})}")
    print(f"\tmethod PATCH: {collection({'method': 'PATCH'})}")
    print(f"\tmethod DELETE: {collection({'method': 'DELETE'})}")
    print(f"{collection({'method': 'GET', 'path': '/status'})} status check")

    print("IPs:")
    client = pymongo.MongoClient('mongodb://127.0.0.1:27017')
    logs = client.logs.nginx
    ips = logs.aggregate(
            [{"$group": {"_id": "$ip", "count": {"$sum": 1}}},
                {"$sort": {"count": -1}}])
    count = 0
    for ip in ips:
        if count == 10:
            break
        print(f"\t{ip.get('_id')}: {ip.get('count')}")
        count += 1


if __name__ == "__main__":
    main()

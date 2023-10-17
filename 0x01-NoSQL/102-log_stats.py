#!/usr/bin/env python3
"""Module containing script that returns Nginx stats stored in MongoDB"""
import pymongo


def collection(db: dict) -> int:
    """Function to retrieve logs information"""
    client = pymongo.MongoClient('mongodb://127.0.0.1:27017')
    logs = client.logs.nginx
    return logs.count_documents(db)


def top_ips():
    """Function to retrieve the top 10 most present IPs"""
    client = pymongo.MongoClient('mongodb://127.0.0.1:27017')
    logs = client.logs.nginx

    pipeline = [
        {"$group": {"_id": "$ip", "count": {"$sum": 1}}},
        {"$sort": {"count": -1}},
        {"$limit": 10}
    ]

    result = list(logs.aggregate(pipeline))
    return result


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
    top_ip_data = top_ips()
    for ip_entry in top_ip_data:
        ip = ip_entry["_id"]
        count = ip_entry["count"]
        print(f"\t{ip}: {count}")


if __name__ == "__main__":
    main()

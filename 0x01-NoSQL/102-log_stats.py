#!/usr/bin/env python3
"""Module containing a script that returns Nginx stats stored in MongoDB"""
import pymongo


def collection(db: dict) -> (int, list):
    """Function to retrieve logs information and top 10 IPs"""
    client = pymongo.MongoClient('mongodb://127.0.0.1:27017')
    logs = client.logs.nginx
    count = logs.count_documents(db)
    ips = logs.aggregate([
        {"$match": db},
        {"$group": {"_id": "$ip", "count": {"$sum": 1}},
         },
        {"$sort": {"count": -1}},
        {"$limit": 10}])
    top_ips = [(ip.get('_id'), ip.get('count')) for ip in ips]
    return count, top_ips


def main():
    """Function that returns stats about Nginx logs stored in MongoDB"""
    total_logs, _ = collection({})  # Get the total logs count
    print(f"{total_logs} logs")
    print("Methods:")
    print(f"\tmethod GET: {collection({'method': 'GET'})[0]}")
    print(f"\tmethod POST: {collection({'method': 'POST'})[0]}")
    print(f"\tmethod PUT: {collection({'method': 'PUT'})[0]}")
    print(f"\tmethod PATCH: {collection({'method': 'PATCH'})[0]}")
    print(f"\tmethod DELETE: {collection({'method': 'DELETE'})[0]}")
    request = {'method': 'GET', 'path': '/status'}
    response = collection(request)
    print(f"{response[0]} status check")

    _, top_ips = collection({})  # Get the top 10 IPs
    print("IPs:")
    for ip, count in top_ips:
        print(f"\t{ip}: {count}")


if __name__ == "__main__":
    main()

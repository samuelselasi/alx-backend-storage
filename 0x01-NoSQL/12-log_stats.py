#!/usr/bin/env python3
"""Script that returns Nginx logs stats stored in MongoDB"""
import pymongo

"""
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
"""


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


if __name__ == "__main__":
    main()

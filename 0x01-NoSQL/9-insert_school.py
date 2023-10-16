#!/usr/bin/env python3
"""Module containing function that inserts a new document in a collection"""
import pymongo


def insert_school(mongo_collection, **kwargs):
    """Function that inserts a new document in a collection with kwargs"""

    return mongo_collection.insert_one(kwargs).inserted_id

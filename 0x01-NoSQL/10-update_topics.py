#!/usr/bin/env python3
"""Module containing function that updates topics of school doc with name"""
import pymongo


def update_topics(mongo_collection, name, topics):
    """Function that updates school topics based on name"""

    return mongo_collection.update_many(
            {"name": name}, {"$set": {"topics": topics}})

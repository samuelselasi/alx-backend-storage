#!/usr/bin/env python3
"""Module containing function that returns the list of schools with topics"""
import pymongo


def schools_by_topic(mongo_collection, topic):
    """Function that returns list of schools with a specific topic"""

    return mongo_collection.find({"topics": topic})

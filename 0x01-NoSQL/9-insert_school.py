#!/usr/bin/env python3
"""
Task 9's moongo db document
"""


def insert_school(mongo_collection, **kwargs):
    """
    Inserts a new document
    """
    return mongo_collection.insert_one(kwargs).inserted_id
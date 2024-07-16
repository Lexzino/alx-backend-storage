#!/usr/bin/env python3
"""
Task 8's mongo document 
"""


def list_all(mongo_collection):
    """
    Lists all documents in a collection
    """
    return list(mongo_collection.find())
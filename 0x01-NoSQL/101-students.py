#!/usr/bin/env python3
"""
The top students
"""


def top_students(mongo_collection):
    """
    Function that returns all students sorted by average score
    """
    return mongo_collection.aggregate([
        {"$project": {
            "name": "$name",
            "averageScore": {"$avg": "$topics.score"}
        }},
        {"$sort": {"averageScore": -1}}
    ])
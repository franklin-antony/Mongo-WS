#!/usr/bin/env python
import pymongo

# no need to import sys

# establish a connection to the database
connection = pymongo.MongoClient("mongodb://localhost")

# get a handle to the school database
db = connection.school
scores = db.scores


def find():
    print "find, reporting for duty"
    query = {}
    try:
        cursor = scores.find(query).skip(10)
        cursor.limit(2)
        cursor.sort('student_id', pymongo.ASCENDING)
#        cursor.sort([('student_id', pymongo.ASCENDING),
#                     ('score', pymongo.DESCENDING)])

    except Exception as e:
        print "Unexpected error:", type(e), e

    for doc in cursor:
        print doc


if __name__ == '__main__':
    find()

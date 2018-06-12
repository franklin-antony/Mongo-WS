#!/usr/bin/env python
import pymongo

# no need to import sys

# establish a connection to the database
connection = pymongo.MongoClient("mongodb://localhost")

# get a handle to the school database
db = connection.students
scores = db.grades

index = 1;	
def find():
    print "find, reporting for duty"
    query = {"type":"homework"}
    try:
        cursor = scores.find(query)
#        cursor.sort('score', pymongo.DESCENDING)
        cursor.sort([('student_id', pymongo.ASCENDING),
                     ('score', pymongo.DESCENDING)])

    except Exception as e:
        print "Unexpected error:", type(e), e

    global index;
    for doc in cursor:
        if (index % 2 == 0 and index <> 0):
            print(index)
            print("Deleting this doc : " + str(doc['student_id']) + " score :" + str(doc['score']))
            #del(doc["_id"])
            #db.grades.delete_one(doc)
        else:
            print(doc)
        index = index + 1
		



if __name__ == '__main__':
    find()

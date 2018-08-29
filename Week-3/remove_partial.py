#!/usr/bin/env python
import pymongo

# no need to import sys

# establish a connection to the database
connection = pymongo.MongoClient("mongodb://localhost")

# get a handle to the school database
db = connection.school
scores = db.students

index = 1;	
def find():
    print "find, reporting for duty"
    query = {"scores.type":"homework"}
    try:
        cursor = scores.find(query)
#        cursor.sort('score', pymongo.DESCENDING)
        cursor.sort([('student_id', pymongo.ASCENDING),
                     ('score', pymongo.DESCENDING)])

    except Exception as e:
        print "Unexpected error:", type(e), e

    global index;
    global matched_score_index;
    for doc in cursor:
	print[doc]
	#print(doc['scores'][0])
	#print(doc['scores'][1])
	print(doc['scores'][2])
	print(doc['scores'][3])
	if (doc['scores'][2] > doc['scores'][3]):
		print(str(doc["_id"])+"Doc Scores 2 is greater")
		matched_score_index = 3;
	if (doc['scores'][3] > doc['scores'][2]):
		print(str(doc["_id"])+"Doc Scores 3 is greater")
		matched_score_index = 2;		
	del doc['scores'][matched_score_index]
	print[doc]
	scores.save(doc)
	index = index + 1
		



if __name__ == '__main__':
    find()

#!/usr/bin/env python
import pymongo

# Do not need to import sys

connection = pymongo.MongoClient("mongodb://localhost")

db = connection.test
users = db.users

doc = {'firstname':'Franklin', 'lastname':'Antony'}
print doc
print "Attempting first to insert the document......"

try:
    users.insert_one(doc)
except Exception as e:
    print "first insert failed:", e

print doc
print "Attempting second to insert the document......"

try:
    users.insert_one(doc)
except Exception as e:
    print "second insert failed:", e

print doc


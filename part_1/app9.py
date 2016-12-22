# -*- coding: utf-8 -*-
import pymongo

__author__ = "pkpacheco"

uri = "mongodb://127.0.0.1:27017"
client = pymongo.MongoClient(uri)
database = client['fullstack']
collection = database['students']

students = [student for student in collection.find({})]
# students = [student['mark']for student in collection.find({})]
# students = [student['mark']for student in collection.find({}) if student['mark'] == 100.0]
print (students)

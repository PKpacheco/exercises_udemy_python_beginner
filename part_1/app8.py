# -*- coding: utf-8 -*-
import pymongo

__author__ = "pkpacheco"

uri = "mongodb://127.0.0.1:27017"
client = pymongo.MongoClient(uri)
database = client['fullstack']
collection = database['students']

students = collection.find({})
student_list = []

for student in students:
    student_list.append(student)
    print (student_list)

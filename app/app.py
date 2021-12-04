#!/usr/bin/env python3
import os
import json
import pymongo
from flask import Flask
from flask import request

# from https://medium.com/swlh/inserting-and-reading-mongodb-documents-from-a-python-flask-api-4fa7be61e45

def mongoConnect():
    dbName = "sleeperPy"
    collectionName = "players"
    # connect to mongodb locally
    client = MongoClient()
    # default host/port
    db = client[dbName]
    collection = db[collectionName]
    return db,collection

@app.route("/", methods=['POST'])
def insert_document():
    mongoConnect()
    req_data = request.get_json()
    collection.insert_one(req_data).inserted_id
    return ('', 204)
    
@app.route('/')
def get():
    documents = collection.find()
    response = []
    for document in documents:
        document['_id'] = str(document['_id'])
        response.append(document)
    return json.dumps(response)
    
if __name__ == '__main__':
    app.run()
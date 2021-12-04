#!/usr/bin/env python3
# Proof of concept stub to initalize the full NFL player roster in MongoDB
# Data provided by Sleeper Fantasy Football
import os, requests, json, urllib.request
from pymongo import MongoClient
from pathlib import Path

# Vars
host = "localhost"
port = 27017
dbName = "sleeperPy"
collectionName = "players"
playersFile = "players.json"


def mongoConnect():
    
    client = MongoClient(host,port)
    # default host/port
    db = client[dbName]
    collection = db[collectionName]
    return db,collection

def mongoImport():
    playersPath = Path(playersFile)

    url = "https://api.sleeper.app/v1/players/nfl"

    with urllib.request.urlopen(url) as url:
        data = json.loads(url.read().decode())
        with open(playersFile, 'w') as f:
            json.dump(data,f)
            f.close()

        # clean up existing data if exists
        collection.delete_many({})
        # import new data
        os.system("mongoimport --host " + host + " --port " + str(port) + " --db " + dbName + " --collection " + collectionName +" --file " + playersFile)

db, collection = mongoConnect()
mongoImport()

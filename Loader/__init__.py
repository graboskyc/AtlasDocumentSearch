import pymongo
from bson.objectid import ObjectId
import gridfs
import threading
import os
from bson.json_util import dumps
from datetime import datetime
import tika
from tika import parser

# configure connection to mongodb
connStr = "mongodb+srv://..."
conn = pymongo.MongoClient(connStr)
handle = conn["tika"]["extracted"]
fs = GridFS(conn["tika"], 'tika')
path = "/mnt/c/Users/chris/GITHUB/AtlasDocumentSearch/TikaSrc"

handle.delete_many({})

for file in os.listdir(path):
    fh = open(file,"rb")
    gfsid = fs.put(fh, filename=file)
    parsed = parser.from_file(file)
    parsed["gsky"] = {}
    parsed["gsky"]["filename"] = file
    parsed["gsky"]["gridfsid"] = gfsid
    handle.insert_one(parsed)


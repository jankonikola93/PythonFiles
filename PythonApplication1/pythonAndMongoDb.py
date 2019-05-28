import pymongo
myClient = pymongo.MongoClient("mongodb://localhost:27017/")
def GetListOfDatabases():
    #import pymongo
    #myClient = pymongo.MongoClient("mongodb://localhost:27017/")
    print(myClient.list_database_names())
    #print(type(myClient.list_database_names())) #type is list

def GetListOfCollectionsInDatabase(databaseName):
    #import pymongo
    #myClient = pymongo.MongoClient("mongodb://localhost:27017/")
    db = myClient[databaseName]
    collections = db.list_collection_names()
    print(collections)

def GetRecordsFromCollection(databaseName, collectionName):
    db = myClient[databaseName]
    collection = db[collectionName]
    cursor = collection.find({})
    #print(type(cursor)) # tip je pymongo cursor
    for x in cursor:
        print(x)

def InsertOne(databaseName, collectionName, objectToInsert):
    db = myClient[databaseName]
    collection = db[collectionName]
    try:
        result = collection.insert_one(objectToInsert)
        print(result.inserted_id)
    except:
        print("Doslo je do greske")

def UpdateOne(databaseName, collectionName, objectToUpdate, newValues):
    db = myClient[databaseName]
    collection = db[collectionName]
    query = objectToUpdate
    try:
        collection.update_one(query, newValues)
        print("Uspesno")
    except:
        print("Doslo je do greske")
    
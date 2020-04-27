import pymongo
import os
import sys
import pprint

def main():
    connection_string = os.environ["MONGO_CONNECTION_STRING"]
    db_name = os.environ["MONGO_DBNAME"]
   
    client = pymongo.MongoClient(connection_string)
    db = client[db_name]
    collection = db['test88'] #1. put the name of your collection in the quotes
    document = {"name" : "Brandon", "birthday" : "10/6/03"}
    #2. add a document to your collection using the insert_one method
    docs = db.document
    collection_id = docs.insert_one(document)
    #3. print the number of documents in the collection
    print(collection.count_documents({}))
    #4. print the first document in the collection
    print(collection.find_one())
    #5. print all documents in the collection
    for document in docs.find():
        pprint.pprint(document)
    #6. print all documents with a particular value for some attribute
    for document in docs.find({"birthday" : "10/6/03"}):
        pprint.pprint(document)
    #ex. print all documents with the birth date 12/1/1990
   
   
if __name__=="__main__":
    main()

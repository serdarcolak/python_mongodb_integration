import pymongo
from pymongo import MongoClient
from bson import ObjectId

#MongoDB Atlas Cloud

connect = MongoClient("mongodb+srv://admin:<password>@cluster-first.ohspzff.mongodb.net/?retryWrites=true&w=majority&appName=cluster-first")

#Database ve collection bağlantısı
database = connect["testdb"]
collection = database["deneme"]


#insert işlemi
#data = {"name": "serdar2", "number" : 20, "country" : "England"}
#collection.insert_one(data)

#Update One
# filterUpdate = {"name":"serdarupdate"}
# dataUpdate = {"$set":{"number":15, "country":"England"}}
# collection.update_one(filterUpdate,dataUpdate)

#Update Many
#name alanında '$regex : '^s' S ile başlayanları update et'
#'$options':'i' büyük küçük harf duyarlılığını kaldır
# filterUpdate = {'name': {'$regex': '^s', '$options': 'i'}}
# dataUpdate = {'$set':{'number':10, 'country':'Turkeyupdate'}}
# collection.update_many(filterUpdate, dataUpdate)

#Delete
# filterDelete = {'_id': ObjectId('6666c296ce1faaa3c920617c')}
# collection.delete_one(filterDelete)

#Data Read
documents = collection.find().sort('country')

#Filter Data Read
#documents = collection.find({'name':'serdar2'}).sort('country')

for document in documents:
    print(document)

    
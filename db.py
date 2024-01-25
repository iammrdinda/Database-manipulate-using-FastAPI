from pymongo import MongoClient
client=MongoClient("mongodb://localhost:27017")
#client = MongoClient("mongodb+srv://iammrdinda:T1%402m3%404l5@cluster1.tkf1tdq.mongodb.net/")
db=client.Databasename
collection1=db.Collectio_one 
collection2=db.Collection_two
def create(data):
    data=dict(data)
    response=collection1.insert_one(data)
    return str(response.inserted_id)

def create_for_userdetails_db(data):
    data=dict(data)
    response=collection2.insert_one(data)
    return str(response.inserted_id)

def all():
    response=collection1.find({})
    data=[]
    for i in response:
        i["_id"] =str(i["_id"])
        data.append(i)
    return data

def get_one(condition):
    collection_length = collection1.count_documents({})
    if condition > collection_length:
       return {"Error":"Errorrrrr"}
    user = collection1.find_one({"id":condition})
    user["_id"]=str(user["_id"])
    return user

def update(name,data):
    response=collection1.update_one({"name":name},{"$set":data})
    return response.modified_count

def delete(name):
    response=collection1.delete_one({"description":name})
    return response.deleted_count
    


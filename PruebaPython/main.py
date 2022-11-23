import pymongo
import certifi

ca = certifi.where()
client = pymongo.MongoClient("mongodb+srv://Byron:alejo2468@cluster0.qfgmf.mongodb.net/registardu?retryWrites=true&w=majority",tlsCAFile=ca)

db = client.test
print(db)

baseDatos = client["registardu"]
print(baseDatos.list_collection_names())

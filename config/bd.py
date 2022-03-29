from pymongo import MongoClient

mongo_url ='mongodb+srv://mirimiri11:<password>@cluster0.gzt7z.mongodb.net/myFirstDatabase?retryWrites=true&w=majority'

conn = MongoClient(mongo_url)

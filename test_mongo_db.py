from pymongo import MongoClient

uri = "mongodb+srv://mdsalmankhan41868_db_user:<@password>@cluster0.h0uybm0.mongodb.net/?appName=Cluster0"

client = MongoClient(uri)

try:
    client.admin.command("ping")
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)
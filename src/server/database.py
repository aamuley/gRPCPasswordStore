import pymongo
# Based on code from https://www.mongodb.com/languages/python tutorial
def get_database():
 
   # Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
    client = pymongo.MongoClient('mongodb://mongodb:27017/', connect=True) 
    db = client["SecretStore"] #Db name = SecretStore
    # db.authenticate("admin", "VRuAd2Nvmp4ELHh5") 
    if "secrets" not in client.list_database_names():
        print("Error connecting to MongoDB or creating DB")
    else:
        print("Connected to MongoDB")
 
   # Create the database for our example (we will use the same database throughout the tutorial
    return db
def get_collection():
    return get_database()['secrets']
# This is added so that many files can reuse the function get_database()
if __name__ == "__main__":   
  
   # Get the database
   dbname = get_database()


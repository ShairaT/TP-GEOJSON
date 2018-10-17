from pymongo import MongoClient
class DB():

    __instance = None
    client = MongoClient()
    db = client["Aeropuertos_del_mundo"]
    collection = db["Aeropuertos"]

    def __new__(cls):
        if DB.__instance is None:
            DB.__instance = object.__new__(cls)
        return DB.__instance
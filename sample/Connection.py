from pymongo import MongoClient,errors
class Conection(object):
    client = None
    @staticmethod
    def conected():
        Conection.client= MongoClient()
        return Conection.client.BaseTesting
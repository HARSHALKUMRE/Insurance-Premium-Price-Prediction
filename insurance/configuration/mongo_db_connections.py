import os
import sys
from insurance.logger import logging
from insurance.exception import CustomException
from insurance.constant.database import DATABASE_NAME, COLLECTION_NAME
from insurance.constant.env_variable import MONGODB_URL_KEY
import pymongo
from pymongo import MongoClient
from pymongo.collection import Collection
from pymongo.database import Database
from pandas import DataFrame
from json import loads
import certifi

ca = certifi.where()

class MongoDBClient:
    """
    Class Name :   export_data_into_feature_store
    Description :   This method exports the dataframe from mongodb feature store as dataframe 
    
    Output      :   connection to mongodb database
    On Failure  :   raises an exception
    """
    client = None

    def __init__(self, database_name=DATABASE_NAME) -> None:
        try:
            if MongoDBClient.client is None:
                mongo_db_url = os.getenv(MONGODB_URL_KEY)
                #mongo_db_url = "mongodb+srv://hacktech:harshal@cluster0.pli36wz.mongodb.net/?retryWrites=true&w=majority"
                if mongo_db_url is None:
                    raise Exception(f"Environment key: {MONGODB_URL_KEY} is not set.")
                MongoDBClient.client = pymongo.MongoClient(mongo_db_url, tlsCAFile=ca)
            self.client = MongoDBClient.client
            self.database = self.client[database_name]
            self.database_name = database_name
        except Exception as e:
            raise CustomException(e, sys) from e
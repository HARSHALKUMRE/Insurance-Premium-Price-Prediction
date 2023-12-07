from pymongo import MongoClient
import pandas as pd
from json import loads
import os


data_frame = pd.read_csv(r"G:\100-days-of-dl\Krish_Naik\FSDS_Ineuron_Course\projects\Insurance-Premium-Price-Prediction\notebooks\data\insurance.csv")

records = list(loads(data_frame.T.to_json()).values())

client = MongoClient("mongodb+srv://hacktech:harshal@cluster0.pli36wz.mongodb.net/?retryWrites=true&w=majority")

database_name = client["Harshal"]

collection = database_name["insurance"]

collection.insert_many(records)

for i in collection.find():
    print(i)
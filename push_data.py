#should be run after the connection is checked from test_mongodb.py

import os
import sys
import json

from dotenv import load_dotenv
load_dotenv()  #Load my secret values and environment variables from the .env file so I can use them safely in Python.

MONGO_DB_URL=os.getenv("MONGO_DB_URL")    #The getenv() function returns a pointer to the string containing the value for the specified varname in the current environment
print(MONGO_DB_URL)

import certifi      #python package that provides a set of root certificates.its used by python libraries to make a secure https connection
ca=certifi.where()  # it retrieves that part to the bundle of certificates,ca means certificate authorities

import pandas as pd
import numpy as np
import pymongo
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging

class NetworkDataExtract():
    def __init__(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e,sys)
        
    #our aim is to read the datset and convert it inhto json file

    def csv_to_json_convertor(self,file_path):
        try:
            data=pd.read_csv(file_path)
            data.reset_index(drop=True,inplace=True)
            records=list(json.loads(data.T.to_json()).values())   #T is for transposing
            return records

        except Exception as e:
            raise NetworkSecurityException(e,sys)
        

    def insert_data_mongodb(self,records,database,collection):
        try:
            self.database=database
            self.collection=collection
            self.records=records

            self.mongo_client=pymongo.MongoClient(MONGO_DB_URL)
            self.database=self.mongo_client[self.database]
            self.collection=self.database[self.collection]

            self.collection.insert_many(self.records)

            return len(self.records)
        except Exception as e:
            raise NetworkSecurityException(e,sys) 
    

if __name__=="__main__":
    FILE_PATH=r"Network_Data/phisingData.csv"
    DATABASE="SREESDB"
    Collection="NetworkData"
    networkobj=NetworkDataExtract()
    records= networkobj.csv_to_json_convertor(file_path=FILE_PATH)
    print(records)
    no_of_records=networkobj.insert_data_mongodb(records,DATABASE,Collection)

    print(no_of_records)



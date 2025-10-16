import os
import sys
import numpy as np
import pandas as pd


#defining common constant variables for training pipeline
TARGET_COLUMN:str= "RESULT"       #The label column name in your dataset (what models will predict).
PIPELINE_NAME: str="NetworkSecurity"   #readable pipeline name. Used to create organized artifact directories (e.g., Artifacts/NetworkSecurity/...)
ARTIFACT_DIR:str="Artifacts"            #The top-level folder where all outputs of the pipeline are stored (data files, logs, model files, etc).
FILE_NAME:str="phisingData.csv"

TRAIN_FILE_NAME:str= "train.csv"
TEST_FILE_NAME:str= "test.csv"


#Data ingestion related constants start with varname DATA_INGESTION
DATA_INGESTION_COLLECTION_NAME:str ="NetworkData"     #The name of the MongoDB collection (if source is MongoDB). Data ingestion will query this collection.
DATA_INGESTION_DATABASE_NAME:str ="SREESDB"           #The MongoDB database name to connect to.
DATA_INGESTION_DIR_NAME:str ="data_ingestion"         #Subfolder under the artifact directory dedicated to data ingestion outputs.
DATA_INGESTION_FEATURE_STORE_DIR:str ="feature_store" #Subfolder within the data_ingestion directory where the raw/feature store CSVs (e.g., raw.csv / phisingData.csv) are stored.
DATA_INGESTION_INGESTED_DIR:str ="ingested"           #Subfolder where cleaned & split data (train/test) are stored.
DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO:float =0.2     #Fraction used for splitting (here 20% for test).


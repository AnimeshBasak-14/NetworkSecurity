import pandas as pd
from src.entity.artifact_entity import DataIngestionArtifact
from src.exception.exception import NetworkSecurityException
from src.logging.logger import logging


## configuration of the Data Ingestion Config


from src.entity.config_entity import DataIngestionConfig

import os
import sys
import numpy as np
import pymongo
from typing import List
from sklearn.model_selection import train_test_split

from dotenv import load_dotenv
load_dotenv()

MONGO_DB_URI = os.getenv("MONGO_DB_URI")


class DataIngestion:
    def __init__(self, data_ingestion_config: DataIngestionConfig): 
        try:
            self.data_ingestion_config = data_ingestion_config    
        except Exception as e:
            raise NetworkSecurityException(e, sys)


    def export_collection_as_dataframe(self):
        
        """
        This function is used to export the collection from the MongoDB database as a dataframe.
        """
        
        try:
            database_name = self.data_ingestion_config.database_name
            collection_name = self.data_ingestion_config.collection_name
            self.mongo_client = pymongo.MongoClient(MONGO_DB_URI)
            collection = self.mongo_client[database_name][collection_name]
            
            df = pd.DataFrame(list(collection.find()))
            if "_id" in df.columns:
                df.drop(columns=["_id"], inplace=True)
            df.replace({"na": np.nan}, inplace=True)
            return df
        except Exception as e:
            raise NetworkSecurityException(e, sys)
        
        
    def export_data_into_features_store(self, dataframe: pd.DataFrame):
        """
        This function is used to export the dataframe into the features store.
        """
        try:
            feature_store_file_path = self.data_ingestion_config.feature_store_file_path
            # creating folder
            dir_path = os.path.dirname(feature_store_file_path)
            if not os.path.exists(dir_path):
                os.makedirs(dir_path,exist_ok=True)
            dataframe.to_csv(feature_store_file_path, index=False, header=True)
            return dataframe
        except Exception as e:
            raise NetworkSecurityException(e, sys)


    def split_data_as_train_test(self, dataframe: pd.DataFrame):
        """
        This function is used to split the data into train and test.
        """
        try:
            train_set, test_set = train_test_split(
                dataframe, 
                test_size=self.data_ingestion_config.train_test_split_ratio, 
                random_state=self.data_ingestion_config.random_state
                )
            logging.info(
                "Performed train test split on the dataframe."
                )
            
            logging.info(
                "Exited split_data_as_train_testmethod of Data_Ingestion class"
                )
            
            dir_path = os.path.dirname(self.data_ingestion_config.training_file_path)
            
            if not os.path.exists(dir_path):   
                os.makedirs(dir_path,exist_ok=True)
            logging.info(
                "Exporting train and test file path"
            )
            
            train_set.to_csv(
                self.data_ingestion_config.training_file_path,
                index=False, header=True)
            
            test_set.to_csv(
                self.data_ingestion_config.testing_file_path,
                index=False, header=True)
            
            logging.info(
                "Exported train and test file path"
            )
            
            
        except Exception as e:
            raise NetworkSecurityException(e, sys)


    def initiate_collection_as_dataframe(self):
        try:
            dataframe = self.export_collection_as_dataframe()
            dataframe = self.export_data_into_features_store(dataframe)
            self.split_data_as_train_test(dataframe)
            
            dataingestionartifact = DataIngestionArtifact(
                trained_file_path=self.data_ingestion_config.training_file_path,
                test_file_path=self.data_ingestion_config.testing_file_path
            )
            return dataingestionartifact
        except Exception as e:
            raise NetworkSecurityException(e, sys)
        
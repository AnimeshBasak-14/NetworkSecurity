from datetime import datetime
import os
import numpy as np
import pandas as pd


"""
Define common constants variables for training pipeline
"""

TARGET_COLUMN: str = "Result"
PIPELINE_NAME: str = "src"
ARTIFACT_DIR: str = "Artifacts"
FILE_NAME: str = "phisingData.csv"

TRAIN_FILE_NAME: str = "train.csv"
TEST_FILE_NAME: str = "test.csv"


"""
Data Ingestion related constants start with DATA_INGESTION VAR NAME
"""


DATA_INGESTION_DATABASE_NAME: str = "ANIMESHDB"
DATA_INGESTION_COLLECTION_NAME: str = "NETWORKDATA"
DATA_INGESTION_DIR_NAME: str = "data_ingestion"
DATA_INGESTION_FEATURE_STORE_DIR: str = "feature_store"
DATA_INGESTION_INGESTED_DIR: str = "ingested"
DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO: float = 0.2
DATA_INGESTION_RANDOM_STATE: int = 42


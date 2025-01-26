from src.components.data_ingestion import DataIngestion 
from src.exception.exception import NetworkSecurityException
from src.logging.logger import logging
from src.entity.config_entity import DataIngestionConfig
from src.entity.config_entity import TrainingPipelineConfig


if __name__ == "__main__":
    try:
        TrainingPipelineConfig = TrainingPipelineConfig()
        data_ingestion_config = DataIngestionConfig(TrainingPipelineConfig)
        data_ingestion = DataIngestion(data_ingestion_config)
        logging.info("Initiating Data Ingestion")
        data_ingestion_artifacts = data_ingestion.initiate_collection_as_dataframe()
        print(data_ingestion_artifacts)
    except NetworkSecurityException as e:
        logging.error(e)
    except Exception as e:
        logging.error(e)
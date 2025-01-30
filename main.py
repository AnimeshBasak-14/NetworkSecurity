from src.components.data_ingestion import DataIngestion
from src.components.data_validation import DataValidation
from src.components.data_transformation import DataTransformation
from src.exception.exception import NetworkSecurityException
from src.logging.logger import logging
from src.entity.config_entity import DataIngestionConfig, DataValidationConfig, DataTransformationConfig
from src.entity.config_entity import TrainingPipelineConfig


if __name__ == "__main__":
    try:
        TrainingPipelineConfig = TrainingPipelineConfig()
        data_ingestion_config = DataIngestionConfig(TrainingPipelineConfig)
        data_ingestion = DataIngestion(data_ingestion_config)
        logging.info("Initiating Data Ingestion")
        data_ingestion_artifacts = data_ingestion.initiate_collection_as_dataframe()
        print(data_ingestion_artifacts)
        logging.info("Data Ingestion Completed")
        data_validation_config = DataValidationConfig(TrainingPipelineConfig)
        data_validation = DataValidation(data_ingestion_artifacts, data_validation_config)
        logging.info("Initiating Data Validation")
        data_validation_artifact = data_validation.initiate_data_validation()
        print(data_validation_artifact)
        logging.info("Data Validation Completed")
        data_transformation_config = DataTransformationConfig(TrainingPipelineConfig)
        data_transformation = DataTransformation(data_validation_artifact, data_transformation_config)
        logging.info("Initiating Data Transformation")
        data_transformation_artifact = data_transformation.initiate_data_transformation()
        logging.info("Data Transformation Completed")
        print(data_transformation_artifact)
        
    except NetworkSecurityException as e:
        logging.error(e)
    except Exception as e:
        logging.error(e)
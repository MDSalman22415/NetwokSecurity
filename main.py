from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.exception.exception import NetwokSecurityException
from networksecurity.logging.logger import logging
from networksecurity.components.data_validation import DataValidation
from networksecurity.entity.config_entity import DataIngestionConfig,DataValidationConfig
from networksecurity.entity.config_entity import TrainigPipelineConfig
from networksecurity.constant import training_pipeline
import sys

if __name__=="__main__":
    try:
        logging.info("Enter the try block")
        trainingpipelineconfig = TrainigPipelineConfig()
        dataingestionconfig = DataIngestionConfig(trainingpipelineconfig)
        data_ingestion = DataIngestion(dataingestionconfig)
        logging.info("Initiate the data ingesion")
        dataingesionartifact = data_ingestion.initiate_data_ingestion()
        logging.info("Data Initiate Completed")
        print(dataingesionartifact)
        data_validation_config = DataValidationConfig(trainingpipelineconfig)
        data_validation = DataValidation(dataingesionartifact,data_validation_config)
        logging.info("Initiate the data Validation")
        data_validation_artifact = data_validation.initaite_data_validation()
        logging.info("Data Validation is completed")
        print(data_validation_artifact)
    except Exception as e:
        raise NetwokSecurityException(e, sys)

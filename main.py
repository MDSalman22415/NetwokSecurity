from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.exception.exception import NetwokSecurityException
from networksecurity.logging.logger import logging
from networksecurity.entity.config_entity import DataIngestionConfig
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
        print(dataingesionartifact)
    except Exception as e:
        raise NetwokSecurityException(e, sys)

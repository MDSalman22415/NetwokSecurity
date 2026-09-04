from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.exception.exception import NetwokSecurityException
from networksecurity.logging.logger import logging
from networksecurity.components.data_validation import DataValidation
from networksecurity.entity.config_entity import DataIngestionConfig,DataValidationConfig,DataTransformationConfig,ModelTrainerConfig
from networksecurity.entity.config_entity import DataTransformationConfig
from networksecurity.entity.config_entity import TrainigPipelineConfig
from networksecurity.constant import training_pipeline
from networksecurity.components.data_transformation import DataTransformation
from networksecurity.components.model_trainer import ModelTrainer
# from networksecurity.components.data_transformation import DataTransformation,DataTransformationConfig
import sys

import os
import mlflow

mlflow.set_tracking_uri("sqlite:///mlflow.db")
mlflow.set_experiment("Network Security")
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
        print(data_validation_artifact)
        data_transformation_config=DataTransformationConfig(trainingpipelineconfig)
        logging.info("data Transformation started")
        data_transformation=DataTransformation(data_validation_artifact,data_transformation_config)
        data_transformation_artifact=data_transformation.initiate_data_transformation()
        print(data_transformation_artifact)
        logging.info("data Transformation completed")
        
        logging.info("Model training started")
        model_trainer_config =ModelTrainerConfig(trainingpipelineconfig)
        model_trainer  = ModelTrainer(model_trainer_config=model_trainer_config,data_transform_artifact=data_transformation_artifact)
        model_trainer_artifact = model_trainer.initiate_model_trainer()
        
        logging.info("Model Training artifact created")
    except Exception as e:
        raise NetwokSecurityException(e, sys)

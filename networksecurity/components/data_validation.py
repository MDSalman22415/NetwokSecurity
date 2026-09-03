from networksecurity.entity.artifact_entity import DataIngestionArtifact
from networksecurity.entity.config_entity import DataValidationConfig
from networksecurity.logging.logger import logging
from networksecurity.exception.exception import NetwokSecurityException
from networksecurity.constant.training_pipeline import SCHEMA_FILE_PATH
from scipy.stats import ks_2samp
import pandas,numpy,os,sys
from utils.main_utils.utils import read_yaml_file


class DataValidation:
    def __init__(self,data_ingesion_artifact:DataIngestionArtifact,
                 data_validation_config:DataValidationConfig):
        try:
            self.data_ingestion_artifact = data_ingesion_artifact
            self.data_validation_config = data_validation_config
            self.__schema_config = read_yaml_file(SCHEMA_FILE_PATH)
        except Exception  as e:
            raise NetwokSecurityException(e, sys)
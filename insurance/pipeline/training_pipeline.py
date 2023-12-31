import os, sys
from typing import Tuple

from insurance.components.data_ingestion import DataIngestion
from insurance.components.data_validation import DataValidation
from insurance.entity.config_entity import DataIngestionConfig, DataValidationConfig
from insurance.entity.artifact_entity import DataIngestionArtifact, DataValidationArtifact
from insurance.exception import CustomException
from insurance.logger import logging
from pandas import DataFrame


class TrainingPipeline:
    def __init__(self):
        self.data_ingestion_config = DataIngestionConfig()
        self.data_validation_config = DataValidationConfig()


    def start_data_ingestion(self) -> DataIngestionArtifact:
        """
        This method of TrainPipeline class is responsible for starting data ingestion component
        """
        try:
            logging.info(
                "Entered the start_data_ingestion method of TrainPipeline class"
            )
            logging.info("Getting the data from mongodb")
            data_ingestion = DataIngestion(
                data_ingestion_config = self.data_ingestion_config
            )
            data_ingestion_artifact = data_ingestion.initiate_data_ingestion()
            logging.info("Got the train_set and test_set from mongodb")
            logging.info(
                "Exited the start_data_ingestion method of TrainPipeline class"
            )
            return data_ingestion_artifact
        except Exception as e:
            raise CustomException(e, sys) from e

    def start_data_validation(self, data_ingestion_artifact: DataIngestionArtifact) -> DataValidationArtifact:
        """
        This method of TrainPipeline class is responsible for starting data validation component
        """
        try:
            logging.info(
                "Entered the start_data_validation method of TrainPipeline class"
            )
            logging.info("Getting the data from mongodb")
            data_validation = DataValidation(
                data_ingestion_artifact = data_ingestion_artifact,
                data_validation_config = self.data_validation_config
            )
            data_validation_artifact = data_validation.initiate_data_validation()
            logging.info("Got the train_set and test_set from mongodb")
            logging.info(
                "Exited the start_data_validation method of TrainPipeline class"
            )
            return data_ingestion_artifact
        except Exception as e:
            raise CustomException(e, sys) from e


    def run_pipeline(self,) -> None:
        """
        This method of TrainPipeline class is responsible for running complete pipeline
        """
        try:
            data_ingestion_artifact = self.start_data_ingestion()
            data_validation_artifact = self.start_data_validation(data_ingestion_artifact=data_ingestion_artifact)
        except Exception as e:
            raise CustomException(e, sys) from e
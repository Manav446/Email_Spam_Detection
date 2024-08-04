import os
import sys

import pandas as pd
import nltk
import warnings

import pickle

from src.email_classification.entity.config_entity import DataIngestionConfig
from src.email_classification.constants import constants
from src.email_classification.logger import logging
from src.email_classification.exception import CustomException
from src.email_classification.utils import common

from src.email_classification.config.configuration import ConfigurationManager

nltk.download("punkt")
nltk.download("stopwords")
warnings.filterwarnings("ignore")
logger = logging.getLogger("DataTransformation")

class DataTransformation:
    def __init__(self, data_ingestion_config: DataIngestionConfig) -> None:
        self.data_ingestion_config = data_ingestion_config

    def loading_and_cleaning_data(self):
        logger.info("Entering into loading_and_cleaning_data()..............")
        try:
            data = pd.read_csv(os.path.join(self.data_ingestion_config.unzip_dir, constants.INPUT_FILE_NAME))
            logger.info("File loaded successfully.......")
            logger.info(f"Total records file contains: {data.shape}")
            logger.info("Going to delete duplicates and null records")
            data = data.drop_duplicates()
            data = data.dropna(how="any", axis=0)
            data = data.reset_index(drop=True)
            logger.info(f"After cleaning process total records file contains: {data.shape}")
            logger.info("Only storing 6000 records of each for this task.........")

            data = pd.concat([
                data[data[constants.INPUT_FILE_TARGET_VARIABLE] == "Spam"].sample(6000),
                data[data[constants.INPUT_FILE_TARGET_VARIABLE] == "Ham"].sample(6000)
            ])

            data = data.reset_index(drop=True)
            return data
        except Exception as e:
            raise CustomException(e, sys)
    
    def data_preprocessing(self, words):
        logger.info("Entering into data_preprocessing().........")
        try:
           
            data = self.loading_and_cleaning_data()
            X = common.clean_text(data)
            y = data[constants.INPUT_FILE_TARGET_VARIABLE].values
            with open(os.path.join(
                self.data_ingestion_config.unzip_dir, constants.INPUT_PICKLE_FILE_NAME
            ), "wb") as input_file:
                pickle.dump(X, input_file)  
            
            with open(os.path.join(
                self.data_ingestion_config.unzip_dir, constants.TARGET_PICKLE_FILE_NAME
            ), "wb") as target_file:
                pickle.dump(y, target_file)
                        
        except Exception as e:
            raise CustomException(e, sys)


if __name__ == "__main__":
    config = ConfigurationManager()
    data_ingestion_config = config.get_data_ingestion_config()
    data_ingestion = DataTransformation(data_ingestion_config=data_ingestion_config)
    data_ingestion.loading_and_cleaning_data()
    
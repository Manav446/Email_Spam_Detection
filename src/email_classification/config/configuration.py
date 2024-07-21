from pathlib import Path
import sys
import os

from src.email_classification.constants import constants
from src.email_classification.utils.common import read_yaml, create_directories
from src.email_classification.entity.config_entity import DataIngestionConfig
from src.email_classification.logger import logging
from src.email_classification.exception import CustomException

logger = logging.getLogger("ConfigurationManager")

class ConfigurationManager:
    def __init__(self, 
            config_filePath = constants.CONFIG_FILE_PATH, 
            #params_filePath = constants.PARAMS_FILE_PATH
            ) -> None:
        config_filePath
        #params_filePath 

        self.config = read_yaml(config_filePath)
        #self.params = read_yaml(params_filePath)

        create_directories([self.config.artifacts_root])
    
    def get_data_ingestion_config(self) -> DataIngestionConfig:
        logger.info("Entering into get_data_ingestion_config()........")
        config = self.config.data_ingestion
        create_directories([config.root_dir])
        try:
            data_ingestion_config = DataIngestionConfig(
                root_dir=config.root_dir,
                source_URL=config.source_URL,
                local_data_file=config.local_data_file,
                unzip_dir=config.unzip_dir
            )
        except Exception as exe:
            raise CustomException(exe, sys)
        return data_ingestion_config
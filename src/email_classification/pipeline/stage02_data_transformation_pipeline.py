from src.email_classification.config.configuration import ConfigurationManager
from src.email_classification.components.data_transformation_component import DataTransformation
from src.email_classification.logger import logging

STAGE_NAME = "Data Tranformation stage"

logger = logging.getLogger("DataTransformationPipeline")

class DataTransformationPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataTransformation(data_ingestion_config=data_ingestion_config)
        data = data_ingestion.loading_and_cleaning_data()
        data_ingestion.data_preprocessing(data)


if __name__ == '__main__':
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = DataTransformationPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e
import sys

from src.email_classification.pipeline import stage01_data_ingestion_pipeline, stage02_data_transformation_pipeline

from src.email_classification.logger import logging
from src.email_classification.exception import CustomException

logger = logging.getLogger("MainFile")

STAGE_NAME = "Data Ingestion stage"
try:
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
   data_ingestion = stage01_data_ingestion_pipeline.DataIngestionTrainingPipeline()
   data_ingestion.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
   logger.exception(e)
   raise CustomException(e, sys)

STAGE_NAME = "Data Transformation stage"
try:
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
   data_ingestion = stage02_data_transformation_pipeline.DataTransformationPipeline()
   data_ingestion.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
   logger.exception(e)
   raise CustomException(e, sys)
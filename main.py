from src.dsproject import logger
from src.dsproject.pipeline.data_ingestion_pipeline import DataIngestionPipeline


logger.info("Welcome to the end-to-end ds project")

STAGE_NAME = "Data Ingestion Stage"
try:
    logger.info(f">>>>>>> stage {STAGE_NAME} started <<<<<<")
    obj = DataIngestionPipeline()
    obj.initiate_data_ingestion()
    logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<<\n\nx======x")
except Exception as e:
    logger.exception(e)
    raise e

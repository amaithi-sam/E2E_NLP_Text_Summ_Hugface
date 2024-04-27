from src.textSummarizer.logging import logger 
from src.textSummarizer.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline 


STAGE_NAME = "Data Ingestion State"

try:
    logger.info(f">>>>> stage {STAGE_NAME} started <<<<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>> stage {STAGE_NAME} completed <<<<< \n\n x======================x")

except Exception as e:
    logger.exception(e)
    raise e 

from src.mlProject import logger #calls the logger since the logger is written in __init__.py
from src.mlProject.pipeline.stage_03_data_transformation import DataTransformationTrainingPipeline
from src.mlProject.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from src.mlProject.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from src.mlProject.pipeline.stage_04_model_trainer import ModelTrainerPipeline
from src.mlProject.pipeline.stage_05_model_evaluation import ModelEvaluationPipeline
from pathlib import Path


STAGE_NAME = "Data Ingestion stage"

try:
    logger.info(f"stage >>>>>> {STAGE_NAME} <<<<<<<< has started\n\n")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f"stage >>>>>> {STAGE_NAME} <<<<<<<< has completed\n\n**********")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Data validation Stage"

try:
    logger.info(f"starting <<<<<<<<< {STAGE_NAME} >>>>>>>>>>>")
    obj = DataValidationTrainingPipeline()
    obj.main()
    logger.info(f" <<<<<<<<< {STAGE_NAME} completed >>>>>>>>>>>")
except Exception as e:
       logger.exception(e)
       raise e

STAGE_NAME = "Data Transformation stage"

try:  
    logger.info(f"<<<<<<<<<< {STAGE_NAME} started >>>>>>>>>>>>>")
    obj = DataTransformationTrainingPipeline()
    obj.main()
    logger.info(f"<<<<<<<<<< {STAGE_NAME} completed >>>>>>>>>>>>>")
except Exception as e:
        logger.exception(e)
        raise e

STAGE_NAME = "Model training stage"

try:
    logger.info(f">>>>>>>> {STAGE_NAME} started <<<<<<<<")
    obj= ModelTrainerPipeline()
    obj.main()
    logger.info(f">>>>>>>> {STAGE_NAME} completed <<<<<<<<")
except Exception as e:
    logger.info(e)
    raise(e)


STAGE_NAME = "Model Evaluation stage"

try:
    logger.info(f">>>>>>>>>>{STAGE_NAME} started <<<<<<<<<<")
    obj = ModelEvaluationPipeline()
    obj.main()
    logger.info(f">>>>>>>>>>{STAGE_NAME} completed <<<<<<<<<<")
except Exception as e:
    logger.exception(e)
    raise e

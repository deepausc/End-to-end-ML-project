
from src.mlProject.config.configuration import ConfigurationManager
from src.mlProject import logger
from src.mlProject.components.model_trainer import ModelTrainer

STAGE_NAME = "Model training stage"

class ModelTrainerPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        model_trainer_config = config.get_model_trainer_config()
        model_trainer = ModelTrainer(config=model_trainer_config)
        model_trainer.train()


if __name__ == "__main__":
    try:
        logger.info(f">>>>>>>> {STAGE_NAME} started <<<<<<<<")
        obj= ModelTrainer()
        obj.main()
        logger.info(f">>>>>>>> {STAGE_NAME} completed <<<<<<<<")
    except Exception as e:
        logger.info(e)
        raise(e)
    

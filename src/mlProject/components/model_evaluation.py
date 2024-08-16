import os
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
import pandas as pd
from src.mlProject import logger
from pathlib import Path
import joblib
import numpy as np
import mlflow
import mlflow.sklearn
import json
from src.mlProject.entity.config_entity import ModelEvaluationConfig
from urllib.parse import urlparse
from src.mlProject.utils.common import save_json

class ModelEvaluation:
    def __init__(self, config:ModelEvaluationConfig):
        self.config = config

    def eval_metrics(self, actual, prod):
        rmse = np.sqrt(mean_squared_error(actual,prod))
        mae = mean_absolute_error(actual, prod)
        r2 = r2_score(actual, prod)
        return rmse, mae, r2
    
    def log_into_mlflow(self):
        test_data = pd.read_csv(self.config.test_data_path)
        model = joblib.load(self.config.model_path)

        test_x =test_data.drop([self.config.target_column], axis=1)
        test_y = test_data[self.config.target_column]

        mlflow.set_registry_uri(self.config.mlflow_url)
        tracking_url_type_store = urlparse(mlflow.get_tracking_uri()).scheme

        with mlflow.start_run():
            predicted_quanties = model.predict(test_x)

            rmse, mae, r2 = self.eval_metrics(test_y, predicted_quanties)
            scores = {"rmse":rmse,"mae":mae,"r2":r2}
            save_json(path=Path(self.config.metric_file_name), data=scores)

            mlflow.log_params(self.config.all_params)
            mlflow.log_metric("rmse", rmse)
            mlflow.log_metric("mae", mae)
            mlflow.log_metric("r2", r2)

            if tracking_url_type_store != "file":
                #register the model. There are many other ways to register the model. check documentation
                mlflow.sklearn.log_model(model, "model",registered_model_name="ElasticNetModel")
            else:
                mlflow.sklearn.log_model(model, "model")
# End-to-end_ML-project

#first clone the repository
git clone https://github.com/deepausc/End-to-end-ML-project

# initial set up - order - template.py, requirements.txt, setup.py,

# src/mlProject/**init**.py,main.py, common.py, trials.ipynb

# later on - the workflows

1. update config.yaml
2. update schema.yaml
3. update params.yaml
4. update the entity
5. update the configuration manager in src config
6. update the components
7. update the pipeline
8. update the main.py
9. update the app.py

#Go to Remote/Experiments to get the tracking url used below
MLFLOW_TRACKING_URI = https://dagshub.com/deepa.usc/End-to-end-ML-project.mlflow
MLFLOW_TRACKING_USERNAME = deepa.usc
MLFLOW_TRACKING_PASSWORD=aa7a9f8e15982c917cc4b44702e5cde68639e2b0

#in the terminal
export MLFLOW_TRACKING_URI=https://dagshub.com/deepa.usc/End-to-end-ML-project.mlflow
export MLFLOW_TRACKING_USERNAME=deepa.usc
export MLFLOW_TRACKING_PASSWORD=aa7a9f8e15982c917cc4b44702e5cde68639e2b0

#in jupiter notebook, use
import os
os.environ["MLFLOW_TRACKING_URI"] = "https://dagshub.com/deepa.usc/End-to-end-ML-project.mlflow"
os.environ["MLFLOW_TRACKING_USERNAME"] = "deepa.usc"
os.environ["MLFLOW_TRACKING_PASSWORD"] = "aa7a9f8e15982c917cc4b44702e5cde68639e2b0"

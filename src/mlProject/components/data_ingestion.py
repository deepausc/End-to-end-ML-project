#components
import os
from pathlib import Path
from src.mlProject.entity.config_entity import DataIngestionConfig
import urllib.request as request
import zipfile
from src.mlProject import logger
from src.mlProject.utils.common import get_size

class DataIngestion:
    def __init__(self, config:DataIngestionConfig):
        self.config = config

    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            filename, headers = request.urlretrieve(url=self.config.source_URL,
                                                    filename=self.config.local_data_file)
            logger.info(f"{filename} download with following headers {headers}")
        else:
            logger.info(f"{filename} already exists with file size {get_size(Path(self.config.local_data_file))}")

    def extract_zip_file(self):
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file, "r") as zip_ref:
            zip_ref.extractall(unzip_path)
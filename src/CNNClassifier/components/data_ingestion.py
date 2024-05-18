import os
import zipfile
import gdown
from src.CNNClassifier.logger import logging
from src.CNNClassifier.utils.common import get_size
from src.CNNClassifier.entity.config_entity import DataIngestionConfig

class DataIngestion:
    def __init__(self,config:DataIngestionConfig):
        self.config = config
        
    def download_file(self)->str:
        """
        fetch data from the url
       
        """
        try:
            dataset_url = self.config.source_URL
            zip_download_dir = self.config.local_data_file
            os.makedirs(self.config.root_dir,exist_ok=True)
            logging.info(f"Downloading data from {dataset_url} into file {zip_download_dir}")
            
            file_id = dataset_url.split("/")[-2]
            prefix = "https://drive.google.com/uc?/export=download&id="
            
            gdown.download(prefix+file_id,zip_download_dir)
            
            logging.info(f"Downloaded data from {dataset_url} into file {zip_download_dir}")
            
        except Exception as e:
            raise e
        
    def extract_zip_file(self):
        """
        zip_file_path:str
        Extract zip file into data directory
        function returns none
        
        """
        unzip_path = self.config.unzip_dir
        os.makedirs(self.config.unzip_dir,exist_ok=True)
        
        with zipfile.ZipFile(self.config.local_data_file,'r') as zip_ref:
            zip_ref.extractall(unzip_path)
    

import pandas as pd
import numpy as np
from src.DimondProject.logger import logging
from src.DimondProject.exception import customexception

import os
import sys
from sklearn.model_selection import train_test_split
from dataclasses import dataclass
from pathlib import Path



class dataingestionconfig:
    raw_data_path= os.path.join("artifacts","raw.csv")
    train_data_path= os.path.join("artifacts","train.csv")
    test_data_path= os.path.join("artifacts","test.csv")
    
    
class Savedata():
    def __init__(self):
        self.savedataingestion=dataingestionconfig()
        
        
    def startdataingestion(self):
        logging.info("Here I'm start Data Ingestion")
        
        
        try:
            data=pd.read_csv(Path(os.path.join(self.savedataingestion.raw_data_path_)),exist_ok=True)
            os.makedirs(os.path(os.path.join("notebooks/data","cubic_zirconia.csv")))
            data.to_csv(self.savedataingestion.raw_data_path,index=False)
            logging.info("Here I save data in artifact folder")
            
            
            logging.info("Here Now I performed train test split")
            
            
            train_data,test_data=train_test_split(data,test_size=0.25)
            logging.info("Train test completed")


            train_data.to_csv(self.savedataingestion.train_data_path,index=False)
            test_data.to_csv(self.savedataingestion.test_data_path,index=False)  
            
            
            
            logging.info("Data Ingestion Part completed")
            
            
            
            return (
                
                
                self.savedataingestion.train_data_path,
                self.savedataingestion.test_data_path
                
            )          
            
            
            
        
        
        
        
        
        
        
        
        except Exception as e :
            logging.info("Exception during ocured at data ingestion stage")
            raise customexception(e,sys)
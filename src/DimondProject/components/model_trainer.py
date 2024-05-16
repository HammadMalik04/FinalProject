import pandas as pd
import numpy as np
import os
import sys
from src.DimondProject.logger import logging
from src.DimondProject.exception import customexception
from dataclasses import dataclass
from sklearn.linear_model import LinearRegression, Ridge,Lasso,ElasticNet
from src.DimondProject.utils import evaluate_model
from src.DimondProject.utils import save_object



@dataclass
class ModeltrainConfig:
    training_model_file_path=os.path.join('artifacts','Model.plk')
    
    
    
class ModelTrainer:
    def __init__(self):
        self.Model_trainer_Config=ModeltrainConfig()
        
        
        
        
    def initate_Model_training(self,train_arr,test_arr):
        try:
            logging.info("Spliting Dependent and Independent Variable in train test data ")
            X_train,y_train,X_test,y_test=(
                train_array[:,:-1],
                train_array[:,-1]
                test_array[:,:-1]
                test_array[:,-1]
            )
            
            model={
                'LinearRegression':LinearRegression(),
                'Lasso':Lasso(),
                'Ridge':Ridge(),
                'Elasticnet':ElasticNet()
        }
                
            model_report=evaluate_model(X_train,y_train,X_test,y_test,model)
            print(model_report)
            print('\n=================================================\n')
            best_model_score=max(sorted(model_report.values()))
            
            
            best_model_name = list(model_report.keys())[
                list(model_report.values()).index(best_model_score)
            ]
            
            
            best_model = model[best_model_name]
            print(f'Best Model Found , Model Name : {best_model_name} , R2 Score : {best_model_score}')
            print('\n====================================================================================\n')
            
            
            save_object(
                 file_path=self.model_trainer_config.trained_model_file_path,
                 obj=best_model
            )
          

        except Exception as e:
            logging.info('Exception occured at Model Training')
            raise customexception(e,sys)

            
            
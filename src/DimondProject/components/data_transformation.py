
import os
import sys
import pandas as pd
import numpy as np

from dataclasses import dataclass
from src.DimondProject.exception import customexception
from src.DimondProject.logger import logging




from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from src.DimondProject.utils import save_object

from sklearn.preprocessing import OrdinalEncoder,StandardScaler



@dataclass 
class DatatranformationConfig:
    preprocessor_obj_file_path=os.path.join("artifacts","preprocessor.pkl")
    
    
    class datatranformatio:
        def __init__(self):
            self.savedata=DatatranformationConfig()
            
            
            
            
            
        def startdatatranformation(self):
            try:
                #defind Which column should be  oridinal_encode and which should be scaler
                cate_col=['cut','color','clarity']
                Num_col=['carat','depth','table','x','y','z']
            
            
                #Define the custom ranking each ordinal Variable 
                cut_cateoriges=['Fair','Good','Very Good','Premiun','Ideal']
                color_categories=['D','E','F','G','H','I','J']
                clarity_categories=['I1','SI2','SI1','VS2','VS1','VVS2','VVS1','IF']
                
                
                num_pipeline=Pipeline(
                steps=[
                ('imputer',SimpleImputer(strategy='median')),
                ('scaler',StandardScaler())

                ]

                )
            
                # Categorigal Pipeline
                cat_pipeline=Pipeline(
                steps=[
                ('imputer',SimpleImputer(strategy='most_frequent')),
                ('ordinalencoder',OrdinalEncoder(categories=[cut_cateoriges,color_categories,clarity_categories])),
                ('scaler',StandardScaler())
                ]

                )
            
                preprocessor=ColumnTransformer([
               ('num_pipeline',num_pipeline,Num_col),
               ('cat_pipeline',cat_pipeline,cate_col)
               ])   
            
                return preprocessor
            
            
            except Exception as e :
             logging.info("Exception occured in the initiate_datatranformation")
             raise customexception(e ,sys)
    
    
        def  initializ_data_tranformation(self,train_path,test_path):
            try:
                train_df=pd.read_csv(train_path)
                test_df=pd.read_csv(test_path)
                
                logging.info("train test completed ")
                
                
                preprocess_obj=self.startdatatranformation()
                
                
                
                
                target_column_name='price'
                drop_columns=[target_column_name,'id']
                
                
                input_feature_train_df=train_df.drop(columns=drop_columns,axis=1)
                target_feature_train_df=train_df(target_column_name)
                
                
                
                input_feature_test_df=test_df.drop(columns=drop_columns,axis=1)
                target_feature_test_df=test_df(target_column_name)
                
            
                input_feature_train_arr=preprocess_obj.fit_transform(input_feature_train_df)
                input_feature_test_arr=preprocess_obj.transform(input_feature_test_df)
            
            
                logging.info("Appling perprocessing object on training and test data ")


                train_arr=np.c_[input_feature_train_arr],np.array(target_feature_train_df)  
                test_arr=np.c_[input_feature_test_arr],np.array(target_feature_test_df)  
                
                
                save_object(
                file_path=self.data_transformation_config.preprocessor_obj_file_path,
                obj=preprocess_obj
            )
                
                
                return (
                    
                    
                    train_arr,
                    test_arr
                )      
            
            except Exception as e :
                 
            
import os 
from pathlib import Path


packages_name={'MLproject'}


list_of_file=[
    "github/workflow/.gitkeep",
    f"src/{packages_name}/__init__.py",
    f"src/{packages_name}/component/__init__.py",
    f"src/{packages_name}/component/data_ingestion.py",
    f"src/{packages_name}/component/data_tranformation.py",
    f"src/{packages_name}/component/model_training.py",
    f"src/{packages_name}/pipline/__init__.py",
    f"src/{packages_name}/pipline/training_pipline.py",
    f"src/{packages_name}/pipline/prediction_pipline.py",
    f"src/{packages_name}/logger.py",
    f"src/{packages_name}/exception.py",
    f"src/{packages_name}/utils/__init__.py",
    "notebook/reasearch.ipynb",
    "notebook/data/.gitkeep",
    "setup.py",
    "requirements.txt",
    "init__setup.sh",
    
]

for filepath in list_of_file:
    filepath=Path(filepath)
    filedir,filename=os.path.split(filepath)
    
    
    
if filedir != "" :
    os.makedirs(filedir,exist_ok=True)
    
    
if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
    with open (filepath,"w"):
        pass 


else:
    print("File alreafy Exist")
    
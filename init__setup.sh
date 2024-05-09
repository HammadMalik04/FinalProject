echo [$(date)]: "START"

echo [$(date)]: "Creating Env  with python 3.11.7 version "
conda create --prefix ./env python=3.11.7 -y 
echo [$(date)]: "activate the Enviroment "
source activate ./env 
echo [$(date)]: "installing the dev requirements"

pip install -r requirements.txt 
echo [$(date)]: "END"
import sys 
from dataclasses import dataclass


class customexception(Exception):
    def __init__(self,error_message,error_detalis:sys):
         self.error_message=error_message
         _,_,exc_tb=error_detalis.exc_info()
    
    
    
         self.lineno=exc_tb.tb_lineno
         self.filename=exc_tb.tb_frame.f_code.co_filename
        
        
    def __str__(self):
        return "Error occured in python script name [{0}] filename [{1}] error _message[{1}]".format (
            self.lineno,self.filename, str(self.error_message))
        
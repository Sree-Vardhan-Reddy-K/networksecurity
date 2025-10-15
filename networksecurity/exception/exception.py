import sys
from networksecurity.logging import logger


class NetworkSecurityException(Exception):
    def __init__(self,error_message,error_details:sys): #error_message and error_details come from sys
        self.error_message=error_message
        _,_,exc_tb = error_details.exc_info()   #it gives 3 values, oyut of which we are concerned with the 3rd one only

        self.lineno=exc_tb.tb_lineno
        self.file_name=exc_tb.tb_frame.f_code.co_filename


    def __str__(self):
        return f"Error occurred in python script name [{0}] line number [{1}] error message [{2}]".format(self.file_name,self.lineno,str(self.error_message))
        


if __name__=="__main__":
    try:
        logger.logging.info("Entered the try block")
        a=1/0
        print("this should not be printed",a)
    except Exception as e:
        raise NetworkSecurityException(e,sys)
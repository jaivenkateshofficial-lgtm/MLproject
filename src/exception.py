import sys
import logging
import logger
def error_message_detials(error,error_detials:sys):
    _,_,exc_tb=error_detials.exc_info()
    file_name=exc_tb.tb_frame.f_code.co_filename
    error_message="An exception has occured in the python script name [{0}] the line number [{1}] the error message[{2}]".format(file_name,exc_tb.tb_lineno,str(error))
    return error_message
    
class customException(Exception):
    def __init__(self,error_message,error_detials:sys):
        super().__init__(error_message)
        self.error_message=error_message_detials(error=error_message,error_detials=error_detials)

    def __str__(self):
        return self.error_message
    
if __name__=='__main__':
    try:
        l='a'
        l/5
    except Exception as e:
        logging.info(f"The exeception occured{e}")
        raise customException(e,sys)
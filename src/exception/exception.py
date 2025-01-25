import sys
from src.logging import logger
class NetworkSecurityException(Exception):
    def __init__(self, error_message, error_details:sys):
        self.error_message = error_message
        _, _, exc_tb = error_details.exc_info()

        self.line_number = exc_tb.tb_lineno
        self.file_name = exc_tb.tb_frame.f_code.co_filename
        
    def __str__(self):
        return "NetworkSecurityException: Error occured in python script name [{0}] line number [{1}] error message [{2}]".format(
            self.file_name, self.line_number, str(self.error_message))
        
if __name__ == '__main__':
    try: 
        logger.logging.info("This is a test log IN TRY BLOCK")
        a = 1/0
        print("This line will not be printed")
    except Exception as e:
        raise NetworkSecurityException(e, sys)
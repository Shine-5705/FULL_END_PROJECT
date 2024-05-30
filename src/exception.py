# this is for the exception if we will use any try catch i other file then we can use this to solve this


import sys
#This module provides access to some variables used or maintained by the interpreter and to functions that interact strongly with the interpreter.


#whenever an exception is raised it will message in the terminal
def error_message_detail(error,error_detail:sys):
   _,_,exc_tb= error_detail.exc_info()  #if will with lin ewich filr
   file_name = exc_tb.tb_frame,f_code.co_filename
   error_message = "error occured in python script mname [{0}] line numvber [{1}] error measssage [{2}]"
   file_name,exc_tb.tb_lineno.str(error)
   return error_message


class CUstomException(Exception):
   def __init__(self, error_message,errror_detail:sys):
      super().__init__(error_message)
      self.error_message = error_message_detail(error_message,error_detail=errror_detail)


   def __str__(self):
       return self.error_message
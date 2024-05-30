import logging
from datetime import datetime
import os

LOG_FILE = f"{datetime.now.starttime('%m_%d_%Y_&H_%M_%S')}.log"

logs_path = os.path.join(os.getcwd(),"logd",LOG_FILE)

os.makedirs(logs_path,exist_ok = True)

LOG_FILE_PAth = os.path.join(logs_path,LOG_FILE)

logging.basicConfig(

    filename=LOG_FILE_PAth,
    format="[ %(asctime)s ] %(lineno)d &(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)
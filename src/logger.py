import logging
import os
from datetime import datetime

# write the log file
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"# file name
logs_path=os.path.join(os.getcwd(),"logs",LOG_FILE)# create repository logs and join paths according to the convention
os.makedirs(logs_path,exist_ok=True)

LOG_FILE_PATH=os.path.join(logs_path,LOG_FILE)# join the both PATH AND FILE

#configuration des logs
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

#if __name__=="__main__":
#    logging.info("Logging has started")
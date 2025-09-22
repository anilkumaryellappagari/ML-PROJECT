import logger
import os 
from datetime import datetime

LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
logs_path=os.path.jion(os.getcwd(),"logs",LOG_FILE)
os.makedirs(logs_path,exits_ok=True)

LOG_FILE_PATH=os.path.jion(logs_path,LOG_FILE )

logging.basicConfig(
    filename=LOG_FILE_PATH,
    formate="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s" - %(message)s",
    level1=logging.INFO, 


)


if __name__=="__main__":
    logging.info("logging has started")

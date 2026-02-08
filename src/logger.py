import logging
import os
from datetime import datetime

# Get project root directory (absolute path of this file → go one level up)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(BASE_DIR)

# Create logs directory inside project root
LOGS_DIR = os.path.join(PROJECT_ROOT, "logs")
os.makedirs(LOGS_DIR, exist_ok=True)

# Create log file
LOG_FILE = f"{datetime.now().strftime('%m-%d_%Y_%H-%M-%S')}.log"
LOG_FILE_PATH = os.path.join(LOGS_DIR, LOG_FILE)

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler(LOG_FILE_PATH),
        logging.StreamHandler()
    ]
)

if __name__ == "__main__":
    logging.info("Logging has started")
    print("Log file created at:", LOG_FILE_PATH)

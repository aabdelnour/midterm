import logging
import os
from dotenv import load_dotenv

load_dotenv()

def log_setup():
    if not os.path.exists('logs'):
        os.makedirs('logs')

    log_level = os.getenv('LOG_LEVEL', 'INFO').upper()
    numeric_level = getattr(logging, log_level, logging.INFO)

    logging.basicConfig(level=numeric_level,
                        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                        handlers=[
                            logging.FileHandler("logs/app.log"),
                            logging.StreamHandler()
                        ])

    logger = logging.getLogger(__name__)

    return logger

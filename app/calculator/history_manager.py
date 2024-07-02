import pandas as pd
import os
from dotenv import load_dotenv
import logging

load_dotenv()

# Set up logging
logging.basicConfig(filename='logs/app.log', level=logging.INFO, 
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class HistoryManager:
    def __init__(self):
        logger.info("Initializing HistoryManager")
        self.filepath = os.getenv('HISTORY_FILE_PATH', 'history.csv')
        if not os.path.exists(self.filepath):
            self.history = pd.DataFrame(columns=['operation', 'operand1', 'operand2', 'result'])
            self.save_history()
        else:
            self.load_history()

    def save_history(self):
        logger.info("Executing save_history")
        self.history.to_csv(self.filepath, index=False)
        logger.info(f"History saved to {self.filepath}")

    def load_history(self):
        logger.info("Executing load_history")
        self.history = pd.read_csv(self.filepath)
        logger.info(f"History loaded from {self.filepath}")

    def add_record(self, operation, operand1, operand2, result):
        logger.info("Executing add_record")
        new_record = pd.DataFrame({
            'operation': [operation],
            'operand1': [operand1],
            'operand2': [operand2],
            'result': [result]
        })
        self.history = pd.concat([self.history, new_record], ignore_index=True)
        self.save_history()
        logger.info(f"Record added: {operation} {operand1} {operand2} = {result}")
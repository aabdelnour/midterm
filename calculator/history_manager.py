import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv()

class HistoryManager:
    def __init__(self):
        self.filepath = os.getenv('HISTORY_FILE_PATH', 'history.csv')
        if not os.path.exists(self.filepath):
            self.history = pd.DataFrame(columns=['operation', 'operand1', 'operand2', 'result'])
            self.save_history()
        else:
            self.load_history()

    def save_history(self):
        self.history.to_csv(self.filepath, index=False)

    def load_history(self):
        self.history = pd.read_csv(self.filepath)

    def add_record(self, operation, operand1, operand2, result):
        new_record = pd.DataFrame({
            'operation': [operation],
            'operand1': [operand1],
            'operand2': [operand2],
            'result': [result]
        })
        self.history = pd.concat([self.history, new_record], ignore_index=True)
        self.save_history()

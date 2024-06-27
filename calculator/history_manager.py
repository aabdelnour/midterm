import pandas as pd

class HistoryManager:
    def __init__(self, filepath='history.csv'):
        self.filepath = filepath
        self.history = pd.DataFrame(columns=['operation', 'operand1', 'operand2', 'result'])

    def save_history(self):
        self.history.to_csv(self.filepath, index=False)

    def load_history(self):
        self.history = pd.read_csv(self.filepath)

    def clear_history(self):
        self.history = pd.DataFrame(columns=['operation', 'operand1', 'operand2', 'result'])

    def add_record(self, operation, operand1, operand2, result):
        self.history = self.history.append({
            'operation': operation,
            'operand1': operand1,
            'operand2': operand2,
            'result': result
        }, ignore_index=True)

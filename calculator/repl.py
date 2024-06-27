from calculator.calculator import Calculator
from calculator.history_manager import HistoryManager
from calculator.logging_config import logger

def repl():
    calculator = Calculator()
    history_manager = HistoryManager()
    while True:
        command = input("> ").strip().lower()
        if command in ['exit', 'quit']:
            logger.info("Exiting REPL")
            break
        if command == "menu":
            logger.info("Displaying menu")
            print("Available commands: add, subtract, multiply, divide, history, save_history, load_history, clear_history")
            continue
        if command == "save_history":
            history_manager.save_history()
            logger.info("History saved")
            print("History saved.")
            continue
        if command == "load_history":
            history_manager.load_history()
            logger.info("History loaded")
            print("History loaded.")
            continue
        if command == "clear_history":
            history_manager.clear_history()
            logger.info("History cleared")
            print("History cleared.")
            continue
        try:
            if command.startswith('add'):
                _, x, y = command.split()
                result = calculator.add(float(x), float(y))
                history_manager.add_record('add', x, y, result)
                print(result)
            elif command.startswith('subtract'):
                _, x, y = command.split()
                result = calculator.subtract(float(x), float(y))
                history_manager.add_record('subtract', x, y, result)
                print(result)
            elif command.startswith('multiply'):
                _, x, y = command.split()
                result = calculator.multiply(float(x), float(y))
                history_manager.add_record('multiply', x, y, result)
                print(result)
            elif command.startswith('divide'):
                _, x, y = command.split()
                result = calculator.divide(float(x), float(y))
                history_manager.add_record('divide', x, y, result)
                print(result)
            else:
                logger.warning("Unknown command")
                print("Unknown command")
        except Exception as e:
            logger.error(f"Error: {e}")

if __name__ == "__main__":
    repl()

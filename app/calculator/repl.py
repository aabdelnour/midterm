import logging
import logging
from app import Calculator
from history_manager import HistoryManager

logging.basicConfig(filename='logs/app.log', level=logging.INFO)
logger = logging.getLogger(__name__)

logger.info("This is a test log message")

def start_repl():
    logger.info("Starting REPL")
    calc = Calculator()
    history_manager = HistoryManager()

    while True:
        command = input("Enter command (add, subtract, multiply, divide, history, exit): ")
        logger.info(f"User entered command: {command}")

        if command == "exit":
            logger.info("Exiting REPL")
            break
        elif command in ("add", "subtract", "multiply", "divide"):
            try:
                x = float(input("Enter first number: "))
                y = float(input("Enter second number: "))
                logger.info(f"Operation: {command}, Numbers: {x}, {y}")

                if command == "add":
                    result = calc.add(x, y)
                elif command == "subtract":
                    result = calc.subtract(x, y)
                elif command == "multiply":
                    result = calc.multiply(x, y)
                elif command == "divide":
                    result = calc.divide(x, y)

                print(f"Result: {result}")
                logger.info(f"Result: {result}")
                history_manager.add_record(command, x, y, result)
            except ValueError as e:
                error_msg = f"Error: {str(e)}"
                print(error_msg)
                logger.error(error_msg)
            except Exception as e:
                error_msg = f"Unexpected error: {str(e)}"
                print(error_msg)
                logger.exception(error_msg)
        elif command == "history":
            print(history_manager.history)
            logger.info("Displayed history")
        else:
            print("Unknown command")
            logger.warning(f"Unknown command entered: {command}")

if __name__ == "__main__":
    start_repl()
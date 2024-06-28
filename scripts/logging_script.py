from calculator.calculator_core import Calculator
from calculator.history_manager import HistoryManager
from calculator.logging_config import logger

def main():
    calc = Calculator()
    history_manager = HistoryManager()

    # Perform some calculations
    calc.add(1, 2)
    calc.subtract(5, 3)
    calc.multiply(4, 3)
    try:
        calc.divide(10, 0)
    except ValueError:
        logger.error("Caught division by zero error")

    # Add some history records
    history_manager.add_record('add', 1, 2, 3)
    history_manager.add_record('subtract', 5, 3, 2)
    history_manager.add_record('multiply', 4, 3, 12)

    print("Logging test completed. Check logs/app.log for details.")

if __name__ == "__main__":
    main()

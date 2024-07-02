from calculator.calculator_core import Calculator
from calculator.history_manager import HistoryManager

def start_repl():
    calc = Calculator()
    history_manager = HistoryManager()

    while True:
        command = input("Enter command (add, subtract, multiply, divide, history, exit): ")
        if command == "exit":
            break
        elif command in ("add", "subtract", "multiply", "divide"):
            try:
                x = float(input("Enter first number: "))
                y = float(input("Enter second number: "))
                if command == "add":
                    result = calc.add(x, y)
                elif command == "subtract":
                    result = calc.subtract(x, y)
                elif command == "multiply":
                    result = calc.multiply(x, y)
                elif command == "divide":
                    result = calc.divide(x, y)
                print(f"Result: {result}")
                history_manager.add_record(command, x, y, result)
            except ValueError as e:
                print(f"Error: {e}")
        elif command == "history":
            print(history_manager.history)
        else:
            print("Unknown command")

if __name__ == "__main__":
    start_repl()

from calculator.logging_config import logger

class Calculator:
    def add(self, x, y):
        print("Executing add")
        result = x + y
        logger.info(f"Add: {x} + {y} = {result}")
        return result

    def subtract(self, x, y):
        print("Executing subtract")
        result = x - y
        logger.info(f"Subtract: {x} - {y} = {result}")
        return result

    def multiply(self, x, y):
        print("Executing multiply")
        result = x * y
        logger.info(f"Multiply: {x} * {y} = {result}")
        return result

    def divide(self, x, y):
        print("Executing divide")
        if y == 0:
            logger.error("Divide: Division by zero error")
            raise ValueError("Cannot divide by zero")
        result = x / y
        logger.info(f"Divide: {x} / {y} = {result}")
        return result

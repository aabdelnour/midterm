import logging

logger = logging.getLogger(__name__)

class Calculator:
    def add(self, x, y):
        result = x + y
        logger.info(f"Add: {x} + {y} = {result}")
        return result

    def subtract(self, x, y):
        result = x - y
        logger.info(f"Subtract: {x} - {y} = {result}")
        return result

    def multiply(self, x, y):
        result = x * y
        logger.info(f"Multiply: {x} * {y} = {result}")
        return result

    def divide(self, x, y):
        if y == 0:
            logger.error("Divide: Division by zero error")
            raise ValueError("Cannot divide by zero")
        result = x / y
        logger.info(f"Divide: {x} / {y} = {result}")
        return result
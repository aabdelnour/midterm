import logging
from calculator.logging_config import logger

def main():
    logger.info("This is an info message.")
    logger.warning("This is a warning message.")
    logger.error("This is an error message.")
    print("Logging test completed. Check logs/app.log for details.")

if __name__ == "__main__":
    main()

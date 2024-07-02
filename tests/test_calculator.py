import pytest
import logging
import os
from app.calculator import Calculator

if not os.path.exists('logs'):
    os.makedirs('logs')

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    filename='logs/app.log',
    filemode='a'
)

logger = logging.getLogger(__name__)

@pytest.fixture
def calc():
    return Calculator()

def test_add(calc: Calculator):
    logger.info("Running add test")
    result = calc.add(1, 2)
    assert result == 3
    logger.info(f"Add test result: {result}")

def test_subtract(calc: Calculator):
    logger.info("Running subtract test")
    result = calc.subtract(2, 1)
    assert result == 1
    logger.info(f"Subtract test result: {result}")

def test_multiply(calc: Calculator):
    logger.info("Running multiply test")
    result = calc.multiply(2, 3)
    assert result == 6
    logger.info(f"Multiply test result: {result}")

def test_divide(calc: Calculator):
    logger.info("Running divide test")
    result = calc.divide(6, 2)
    assert result == 3
    logger.info(f"Divide test result: {result}")

def test_divide_by_zero(calc: Calculator):
    logger.info("Running divide by zero test")
    with pytest.raises(ValueError):
        calc.divide(1, 0)
    logger.info("Divide by zero test completed")
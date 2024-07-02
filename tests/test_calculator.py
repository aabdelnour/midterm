import pytest
import logging
from app.calculator import Calculator

logger = logging.getLonger(__name__)

def setup_logging(tmpdir_factory):
    log_file = tmpdir_factory.mktemp("logs").join("test_app.log")
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        filename=str(log_file),
        filemode='w'
    )
    return log_file

def test_add():
    calc = Calculator()
    assert calc.add(1, 2) == 3

def test_subtract():
    calc = Calculator()
    assert calc.subtract(2, 1) == 1

def test_multiply():
    calc = Calculator()
    assert calc.multiply(2, 3) == 6

def test_divide():
    calc = Calculator()
    assert calc.divide(6, 2) == 3

def test_divide_by_zero():
    calc = Calculator()
    with pytest.raises(ValueError):
        calc.divide(1, 0)

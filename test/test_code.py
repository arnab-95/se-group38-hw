import numpy
from src.app import array_addition


def test_method():
    array = array_addition()
    assert isinstance(array, numpy.ndarray)

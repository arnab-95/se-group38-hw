import numpy
import code


def test_method():
    array = code.array_addition()
    assert isinstance(array, numpy.ndarray)

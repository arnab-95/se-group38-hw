import numpy
from code.__init__ import array_addition


def test_method():
    array = array_addition()
    assert isinstance(array, numpy.ndarray)

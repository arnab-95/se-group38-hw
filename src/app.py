import numpy


def array_addition():
    array_1 = numpy.arange(6).reshape(2, 3)
    array_2 = numpy.array([(5, 7.5, 0.05), (11, 13.8, 0)])
    final_array = array_1 + array_2
    return final_array

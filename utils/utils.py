import numpy

def vcol(x: numpy.ndarray) -> numpy.ndarray:
    return x.reshape((x.size, 1))   
import numpy as np
from fuzzing import fuzzing

def bipolar(agents, candidates, distribution):
    left = np.arange(0, candidates).reshape(candidates, 1)
    right = np.flip(left)
    tiled_left = np.tile(left, round(agents*distribution))
    tiled_right = np.tile(right, round(agents*(1-distribution)))
    result = np.concatenate((tiled_left, tiled_right), axis=1)
    # NOTE: Check to see if Candidates of the required number, can lead to floating point error
    # To get around floating point error one can specify the number of entries they want. 
    assert(agents == (round(agents*distribution) + round(agents*(1-distribution))))
    return result


if "__main__" == __name__:
    print(bipolar(10, 5, 0.1))
    print(fuzzing(bipolar(10, 5, 0.5), 1))
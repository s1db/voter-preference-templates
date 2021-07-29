import numpy as np
from fuzzing import fuzzing

def bipolar(candidates, left, right):
    left_profile = np.arange(0, candidates).reshape(candidates, 1)
    right_profile = np.flip(left_profile)
    tiled_left = np.tile(left_profile, left)
    tiled_right = np.tile(right_profile, right)
    result = np.concatenate((tiled_left, tiled_right), axis=1)

    return result


if "__main__" == __name__:
    print(bipolar(10, 5, 0.1))
    print(fuzzing(bipolar(10, 5, 0.5), 1))
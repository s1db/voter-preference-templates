import numpy as np


def fuzzing(pref_profile, fuzzing_constant):
    for i in range(pref_profile.shape[1]):
        for _ in range(fuzzing_constant):
            index = np.random.randint(pref_profile.shape[0]-1)
            temp = pref_profile[index, i]
            pref_profile[index, i] = pref_profile[index+1, i]
            pref_profile[index+1, i] = temp
    return pref_profile


if "__main__" == __name__:
    print(fuzzing())
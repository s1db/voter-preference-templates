from .lex_ordering_permute import nPermute
# import numpy as np 
import random
import numpy as np
# driver program to generate random instances from the permutation function.
# this is to be followed by a random weight generating function.
# this will serve as an input to main.py

def normal_pref_profile(candidates, distribution, is_random):
    base_profile = list(range(candidates))
    result = np.zeros((candidates, 1))
    val = set()
    no_of_permutations = np.math.factorial(candidates)-1
    if is_random:
        while len(val) != len(distribution):
            index = random.randrange(0, no_of_permutations)
            val.add(index)
    else:
        val = range(2, len(distribution)+2)
    for i,x in enumerate(list(val)):
        candidate_votes = np.array(nPermute(base_profile, x)).reshape(candidates, 1)
        tiled_preference = np.tile(candidate_votes, distribution[i])
        result = np.concatenate((result, tiled_preference), axis=1)
    return result[:,1:]

if __name__ == "__main__":
    p = normal_pref_profile(5, [1,1,1,1,1], False)
    print(p)
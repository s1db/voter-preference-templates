from lex_ordering_permute import nPermute
# import numpy as np 
import random
import math
import numpy as np
# driver program to generate random instances from the permutation function.
# this is to be followed by a random weight generating function.
# this will serve as an input to main.py

def normal_pref_profile(candidates, distribution, is_random):
    result = np.zeros((size_of_cluster*no_of_clusters, 1))
    val = set()
    no_of_permutations = np.math.factorial(CANDIDATES)-1
    while len(val) != len(distribution):
        index = random.randrange(0,no_of_permutations)
        val.add(index)
    for i in val:
        r.append(nPermute(range(CANDIDATES), i))
    return result[:,1:]

if __name__ == "__main__":
    pass
from lex_ordering_permute import nPermute
# import numpy as np 
import random
import math
# driver program to generate random instances from the permutation function.
# this is to be followed by a random weight generating function.
# this will serve as an input to main.py

CANDIDATES, UNIQUE_VOTES = 5, 10

# def rand_pref_profile_gen(candidates, samples):
#     assert
    

if __name__ == "__main__":
    r = []
    val = set()
    t = math.factorial(CANDIDATES)-1
    for i in range(10):
        val.add(random.randrange(0,t))
    for i in val:
        r.append(nPermute(range(CANDIDATES), i))
    print(val)
    print(r)
import random
from lex_ordering_permute import nPermute
import numpy as np
from fuzzing import fuzzing

def clustering(size_of_cluster, no_of_clusters, shuffle):
    new_arr = []
    for i in range(no_of_clusters):
        if shuffle:
            new_arr.append(random.sample(list(range(i*size_of_cluster, (i+1)*size_of_cluster)), size_of_cluster))
        else: 
            new_arr.append(list(range(i*size_of_cluster, (i+1)*size_of_cluster)))
    print(new_arr)
    return new_arr

def biased_clustered_profile(size_of_cluster, no_of_clusters, distribution, shuffle, lex_ordered):
    clustered_votes = np.array(clustering(size_of_cluster, no_of_clusters, shuffle))
    previous_profiles = set()
    result = np.zeros((size_of_cluster*no_of_clusters, 1))
    iter = 0
    previous_profiles.add(0)
    for i in distribution:
        if lex_ordered:
            iter += 1
        else:
            while iter in previous_profiles:
                iter = np.random.randint(np.math.factorial(no_of_clusters)-1)+1
                print(iter)
                previous_profiles.add(iter)
                break
        clustered_votes_lex_ordered = clustered_votes[nPermute(list(range(no_of_clusters)), iter)]
        clustered_votes_lex_ordered = clustered_votes_lex_ordered.flatten().reshape(size_of_cluster*no_of_clusters, 1)
        tiled_preference = np.tile(clustered_votes_lex_ordered, i)
        result = np.concatenate((result, tiled_preference), axis=1)
    return result[:,1:]

# Driver Code for testing
if __name__ == "__main__":
    size_of_cluster = 3
    no_of_clusters = 3
    pref_profile = biased_clustered_profile(size_of_cluster, no_of_clusters, [6,3,1], False, True)    
    print(fuzzing(pref_profile, 3))


# A cluster preference template like 60% have the bias to a certain cluster.
# Randomisation within the clusters.
# Think of it like a political spectrum.
# A parameter for the clusters to show a bias in the population
# to check if the social choice functions returns one of the options.
# One for the cluster.
# One for the individual candidates option.
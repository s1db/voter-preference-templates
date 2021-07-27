# Based off of https://www.geeksforgeeks.org/lexicographically-n-th-permutation-string/

# With changes to adapt to lists.

# next_permutation method implementation.
def next_permutation(L):
    n = len(L)
    i = n - 2
    while i >= 0 and L[i] >= L[i + 1]:
        i -= 1
  
    if i == -1:
        return False
  
    j = i + 1
    while j < n and L[j] > L[i]:
        j += 1
    j -= 1
  
    L[i], L[j] = L[j], L[i]
  
    left = i + 1
    right = n - 1
  
    while left < right:
        L[left], L[right] = L[right], L[left]
        left += 1
        right -= 1
  
    return True
  
# Function to print nth permutation
# using next_permute()
def nPermute(l, n):
    l = list(l)
    new_l = []
  
    # Sort the string in lexicographically
    # ascending order
    l.sort()
    j = 2
    # Keep iterating until
    # we reach nth position
    while next_permutation(l):
        new_l = l
        # check for nth iteration
        if j == n:
            break
        j += 1
    # print string after nth iteration
    return new_l
  
# Driver Code
if __name__ == "__main__":
    no_cand = 6
    string = list(range(no_cand))
    n = 5
    print(nPermute(string, n))

# This code is contributed by
# sanjeev2552 and sidhant bhavnani
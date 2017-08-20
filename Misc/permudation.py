from collections import Counter
from math import factorial

def permutation_count(s):
    """Return the number of different permutations of s."""
    s = str(s)
    c = 1
    for i in Counter(s).values():
        c *= factorial(i)
    return factorial(len(s)) // c

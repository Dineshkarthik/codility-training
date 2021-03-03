"""
The Fibonacci sequence is defined using the following recursive formula:

    F(0) = 0
    F(1) = 1
    F(M) = F(M - 1) + F(M - 2) if M >= 2
A small frog wants to get to the other side of a river.
The frog is initially located at one bank of the river (position −1)
and wants to get to the other bank (position N).
The frog can jump over any distance F(K), where F(K) is the K-th Fibonacci number.
Luckily, there are many leaves on the river, and the frog can jump between the leaves,
but only in the direction of the bank at position N.

The leaves on the river are represented in a zero-indexed array A consisting of N integers. Consecutive elements of array A represent consecutive positions from 0 to N − 1 on the river. Array A contains only 0s and/or 1s:

0 represents a position without a leaf;
1 represents a position containing a leaf.
The goal is to count the minimum number of jumps in which the frog can get
to the other side of the river (from position −1 to position N).
The frog can jump between positions −1 and N (the banks of the river) and
 every position containing a leaf.

For example, consider array A such that:

    A[0] = 0
    A[1] = 0
    A[2] = 0
    A[3] = 1
    A[4] = 1
    A[5] = 0
    A[6] = 1
    A[7] = 0
    A[8] = 0
    A[9] = 0
    A[10] = 0
The frog can make three jumps of length F(5) = 5, F(3) = 2 and F(5) = 5.

Write a function:

def solution(A)

that, given a zero-indexed array A consisting of N integers,
returns the minimum number of jumps by which the frog can get to the other side of the river. If the frog cannot reach the other side of the river, the function should return −1.

For example, given:

    A[0] = 0
    A[1] = 0
    A[2] = 0
    A[3] = 1
    A[4] = 1
    A[5] = 0
    A[6] = 1
    A[7] = 0
    A[8] = 0
    A[9] = 0
    A[10] = 0
the function should return 3, as explained above.

Assume that:

N is an integer within the range [0..100,000];
each element of array A is an integer that can have one of the following values: 0, 1.
Complexity:

    expected worst-case time complexity is O(N*log(N));
    expected worst-case space complexity is O(N),
      beyond input storage (not counting the storage required for input arguments).
Elements of input arrays can be modified.
"""


def get_fib_seq_up_to_n(N):
    fib = [0] * (27)
    fib[1] = 1
    for i in range(2, 27):
        fib[i] = fib[i - 1] + fib[i - 2]
        if fib[i] > N:
            return fib[2:i]
        else:
            last_valid = i


def solution(A):
    # you can always step on the other shore, this simplifies the algorithm
    A.append(1)

    fib_set = get_fib_seq_up_to_n(len(A))

    # this array will hold the optimal jump count that reaches this index
    reachable = [-1] * (len(A))

    # get the leafs that can be reached from the starting shore
    for jump in fib_set:
        if A[jump - 1] == 1:
            reachable[jump - 1] = 1

    # iterate all the positions until you reach the other shore
    for idx in range(len(A)):
        # ignore non-leafs and already found paths
        if A[idx] == 0 or reachable[idx] > 0:
            continue

        # get the optimal jump count to reach this leaf
        min_idx = -1
        min_value = 100000
        for jump in fib_set:
            previous_idx = idx - jump
            if previous_idx < 0:
                break
            if reachable[previous_idx] > 0 and min_value > reachable[
                    previous_idx]:
                min_value = reachable[previous_idx]
                min_idx = previous_idx
        if min_idx != -1:
            reachable[idx] = min_value + 1

    return reachable[len(A) - 1]

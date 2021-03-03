"""
For a given array A of N integers and a sequence S of N integers
 from the set {−1, 1}, we define val(A, S) as follows:

val(A, S) = |sum{ A[i]*S[i] for i = 0..N−1 }|

(Assume that the sum of zero elements equals zero.)

For a given array A, we are looking for such a sequence S
 that minimizes val(A,S).

Write a function:

    def solution(A)

that, given an array A of N integers, computes the minimum value of val(A,S)
 from all possible values of val(A,S) for all possible sequences S of N integers
 from the set {−1, 1}.

For example, given array:

  A[0] =  1
  A[1] =  5
  A[2] =  2
  A[3] = -2
your function should return 0, since for S = [−1, 1, −1, 1], val(A, S) = 0,
 which is the minimum possible value.

Assume that:
    N is an integer within the range [0..20,000];
    each element of array A is an integer within the range [−100..100].

Complexity:
    expected worst-case time complexity is O(N*max(abs(A))2);
    expected worst-case space complexity is O(N+sum(abs(A))),
     beyond input storage (not counting the storage required for input arguments).

Elements of input arrays can be modified.
"""


def solution(A):
    # Since S could be 1 or -1, it does not matter that
    # each element in A is positive or negative.
    A = [abs(item) for item in A]
    sumOfA = sum(A)

    # Get the number distribution. So we do not need to try
    # each number for multiple times.
    numbers = {}
    for item in A:
        numbers[item] = numbers.get(item, 0) + 1

    possible = [-1] * (sumOfA // 2 + 1)
    possible[0] = 0

    for number in numbers:  # Try each distinct number
        for trying in range(sumOfA // 2 + 1):
            if possible[trying] >= 0:
                # Can be reached with previous numbers
                possible[trying] = numbers[number]
            elif trying >= number and possible[trying - number] > 0:
                # Cannot be reached with only previous numbers.
                # But could be achieved with previous numbers AND current one.
                possible[trying] = possible[trying - number] - 1

    # Divide the A into two parts: P and Q, with restriction P <= Q.
    # So P <= sumOfA // 2 <= Q. We want the largest possible P, so that
    # Q-P is minimized.
    for halfSum in range(sumOfA // 2, -1, -1):
        if possible[halfSum] >= 0:
            return sumOfA - halfSum - halfSum

    raise Exception("Should never be here!")
    return 0

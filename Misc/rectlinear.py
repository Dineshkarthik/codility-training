"""A rectangle is called rectlinear.

If its edges are all parallel to coordinated axes. Such an rectangle can be
destroyed by specifying the coordinaes of its lower left and upper left
right corners.


Such a rectangle can be described by specifying the coordinated of its lower-left
 and upper-right corners.
Write a function: function solution($K,$L,$M,$N,$P,$Q,$R,$S);
that given eight integers representing two rectilinear rectangles
(one with lower-left corner (K,L) and upper right corner (M,N),
and another with lower-left corner (P,Q) and upper-right corner (R,S)),
returns the area of the sum of the rectangles.
If the rectangles intersect the area of the intersection should be counted only once.
The function should return -1 if the area of the sum exceeds 2,147,483,647.
 For example Given Integers: K= -4 L = 1 M = 2 N = 6 P = 0 Q = -1 R = 4 S = 3
 **the function should return 42** *
 The area of the First rectangle is 30 and the area of the second rectangle is 16
  and the area of their intersection is 4.
  Assume that * K,L,M,N,P,Q,R and S are integers within the
  range [-2147483648...2147483647]. * K<M * L<N * P<R * Q<S
"""

# you can use print for debugging purposes, e.g.
# print "this is a debug message"


def is_overlap(K, L, M, N, P, Q, R, S):
    if R < K or M < P:
        return False
    if S < L or Q > N:
        return False
    return True


def overlap(K, L, M, N, P, Q, R, S):
    if not is_overlap(K, L, M, N, P, Q, R, S):
        return 0
    x = max(0, min(M, R) - max(K, P))
    y = max(0, min(N, S) - max(L, Q))
    return x * y


def area(Lx, Ly, Rx, Ry):
    return (Rx - Lx) * (Ry - Ly)


def solution(K, L, M, N, P, Q, R, S):
    # write your code in Python 2.7
    a1 = area(K, L, M, N)
    a2 = area(P, Q, R, S)
    r = a1 + a2 - overlap(K, L, M, N, P, Q, R, S)
    print r
    return r if r <= 2147483647 else -1

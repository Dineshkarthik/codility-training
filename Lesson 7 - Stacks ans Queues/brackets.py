"""
A string S consisting of N characters is considered to be properly nested
if any of the following conditions is true:

S is empty;
S has the form "(U)" or "[U]" or "{U}" where U is a properly nested string;
S has the form "VW" where V and W are properly nested strings.
For example, the string "{[()()]}" is properly nested but "([)()]" is not.

Write a function:

def solution(S)

that, given a string S consisting of N characters,
returns 1 if S is properly nested and 0 otherwise.

For example, given S = "{[()()]}", the function should return 1 and given
S = "([)()]", the function should return 0, as explained above.

Assume that:

N is an integer within the range [0..200,000];
string S consists only of the following characters: "(", "{", "[", "]", "}" and/or ")".
Complexity:

expected worst-case time complexity is O(N);
expected worst-case space complexity is O(N)
(not counting the storage required for input arguments).
"""

CLOSING = {
    ']': '[',
    ')': '(',
    '}': '{',
}


def solution(S):
    stack = []
    for ch in S:
        if ch in CLOSING:
            if not stack:
                # encountered closing bracket but stack is already empty!
                return 0
            last = stack.pop()
            if last != CLOSING[ch]:
                # wrong bracket encountered
                return 0
        else:
            stack.append(ch)
    if stack:
        # there are still opened brackets on a stack
        return 0
    else:
        return 1

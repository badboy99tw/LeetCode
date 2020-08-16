"""
989. Add to Array-Form of Integer
https://leetcode.com/problems/add-to-array-form-of-integer/

For a non-negative integer X, the array-form of X is an array of its digits in left to right order.  
For example, if X = 1231, then the array form is [1,2,3,1].

Given the array-form A of a non-negative integer X, return the array-form of the integer X+K.

Example 1:

    Input: A = [1,2,0,0], K = 34
    Output: [1,2,3,4]
    Explanation: 1200 + 34 = 1234

Example 2:

    Input: A = [2,7,4], K = 181
    Output: [4,5,5]
    Explanation: 274 + 181 = 455

Example 3:

    Input: A = [2,1,5], K = 806
    Output: [1,0,2,1]
    Explanation: 215 + 806 = 1021

Example 4:

    Input: A = [9,9,9,9,9,9,9,9,9,9], K = 1
    Output: [1,0,0,0,0,0,0,0,0,0,0]
    Explanation: 9999999999 + 1 = 10000000000

Note：

    1 <= A.length <= 10000
    0 <= A[i] <= 9
    0 <= K <= 10000
    If A.length > 1, then A[0] != 0
"""
import itertools
from typing import List


class Solution:
    def toArrayForm(self, K: int) -> List[int]:
        if K == 0:
            return [0]
        result = []
        tmp = K
        while tmp != 0:
            result.insert(0, tmp % 10)
            tmp = int(str(tmp)[:-1] or 0)
        return result

    def addToArrayForm(self, A: List[int], K: int) -> List[int]:
        arrarFormK = self.toArrayForm(K)

        overflow = 0
        reversedResult = []
        for n1, n2 in itertools.zip_longest(A[::-1], arrarFormK[::-1], fillvalue=0):
            newN = n1 + overflow + n2
            overflow = int(newN / 10)
            newN = newN % 10
            reversedResult.append(newN)
        if overflow != 0:
            reversedResult.append(overflow)
        return reversedResult[::-1]


def test():
    s = Solution()

    assert s.addToArrayForm(A=[1, 2, 0, 0], K=34) == [1, 2, 3, 4]

    assert s.addToArrayForm(A=[2, 7, 4], K=181) == [4, 5, 5]

    assert s.addToArrayForm(A=[2, 1, 5], K=806) == [1, 0, 2, 1]

    assert s.addToArrayForm(A=[9, 9, 9, 9, 9, 9, 9, 9, 9, 9], K=1) == [
        1,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
    ]

"""
7. Reverse Integer
https://leetcode.com/problems/reverse-integer/

Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

    Input: 123
    Output: 321

Example 2:

    Input: -123
    Output: -321

Example 3:

    Input: 120
    Output: 21

Note:
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−2^31,  2^31 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.
"""
MAX_NUMBER = pow(2, 31) - 1
MIN_NUMBER = -pow(2, 31)


class Solution:
    def reverse(self, x: int) -> int:
        is_positive = x >= 0
        number = int(str(abs(x))[::-1])
        number = number if is_positive else -number
        if number > MAX_NUMBER:
            return 0
        elif number < MIN_NUMBER:
            return 0
        else:
            return number


def test():
    s = Solution()

    assert s.reverse(123) == 321
    assert s.reverse(-123) == -321
    assert s.reverse(120) == 21
    assert s.reverse(1534236469) == 0

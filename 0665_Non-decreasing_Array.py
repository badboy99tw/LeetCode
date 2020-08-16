"""
665. Non-decreasing Array
https://leetcode.com/problems/non-decreasing-array/

Given an array nums with n integers, your task is to check if it could become non-decreasing by modifying at most 1 element.

We define an array is non-decreasing if nums[i] <= nums[i + 1] holds for every i (0-based) such that (0 <= i <= n - 2).

Example 1:

    Input: nums = [4,2,3]
    Output: true
    Explanation: You could modify the first 4 to 1 to get a non-decreasing array.

Example 2:

    Input: nums = [4,2,1]
    Output: false
    Explanation: You can't get a non-decreasing array by modify at most one element.

Constraints:

    1 <= n <= 10 ^ 4
    - 10 ^ 5 <= nums[i] <= 10 ^ 5
"""
from typing import List


class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        modifiedCount = 0
        for i in range(len(nums)):
            if modifiedCount > 1:
                break

            # window size = 3
            prev = -100000 if i == 0 else nums[i - 1]
            curr = nums[i]
            next_ = 100000 if i == len(nums) - 1 else nums[i + 1]

            if prev <= curr and curr <= next_:
                continue
            elif curr > next_:
                if prev <= next_:  # modify curr
                    nums[i] = prev
                    modifiedCount += 1
                else:  # modify next
                    nums[i + 1] = curr
                    modifiedCount += 1
        return modifiedCount <= 1


def test():
    s = Solution()
    assert s.checkPossibility([4, 2, 3]) is True
    assert s.checkPossibility([4, 2, 1]) is False
    assert s.checkPossibility([-1, 4, 2, 3]) is True
    assert s.checkPossibility([5, 7, 1, 8]) is True
    assert s.checkPossibility([1, 4, 1, 2]) is True

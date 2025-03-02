#Given an integer array nums, find the subarray with the largest sum, and return its sum.

class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        if len(nums) == 0:
            return 0
        absoluteMax = currentMax = float("-inf")
        for number in nums: 
            currentMax = max(number,currentMax+number)
            absoluteMax = max(currentMax,absoluteMax)
        return absoluteMax

#Given a non-empty array of integers nums, every element appears twice except for one. Find that single one
#You must implement a solution with a linear runtime complexity and use only constant extra space.


class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        summation = 0 
        for number in nums:  
            summation = summation ^ number 
        return summation 

i = Solution()
i.singleNumber([2,2,1])

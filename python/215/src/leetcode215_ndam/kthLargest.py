#Given an integer array nums and an integer k, return the kth largest element in the array.

#Note that it is the kth largest element in the sorted order, not the kth distinct element.

#Can you solve it without sorting?
import heapq
class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        if len(nums) == 0:
            return 0 
        heap = nums[:k]
        heapq.heapify(heap)
        
        for num in nums[k:]:
            if num > heap[0]:
                heapq.heappop(heap)
                heapq.heappush(heap, num)
        
        return heap[0]


i = Solution()
print(i.findKthLargest([3,2,3,1,2,4,5,5,6],4))

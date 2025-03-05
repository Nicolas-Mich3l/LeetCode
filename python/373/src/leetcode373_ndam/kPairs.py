#You are given two integer arrays nums1 and nums2 sorted in non-decreasing order and an integer k.

#Define a pair (u, v) which consists of one element from the first array and one element from the second array.

#Return the k pairs (u1, v1), (u2, v2), ..., (uk, vk) with the smallest sums.

#functional but _slow_, can improve this from the brute force solution by switching to a more elegant processing of nums1 and nums2 (rather than the nested for loops). I dont feel like improving this atm :)

class Solution:
    def __init__(self):
        self.pq = []
    def insertPQ(self,num1,num2,k):
        prio = num1 + num2
        self.pq.append([[num1,num2],prio])
        self.pq.sort(key=lambda x: x[1])
        self.pq = self.pq[:k]
    def kSmallestPairs(self, nums1: list[int], nums2: list[int], k: int) -> list[list[int]]:
        for number1 in nums1:
            for number2 in nums2:
                if len(self.pq) <= k:
                    self.insertPQ(number1,number2,k)
                elif number1+number2 < self.pq[-1][1]:
                    self.insertPQ(number1,number2,k)
        out =  [x[0] for x in self.pq]
        return out

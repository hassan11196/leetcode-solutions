# https://leetcode.com/problems/kth-largest-element-in-a-stream/

from heapq import *

class KthLargest(object):

    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.arr = nums
        heapify(self.arr)
        self.k = k
        

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        
        heappush(self.arr, val)
        
        while len(self.arr) > self.k:
            heappop(self.arr)
            
        return self.arr[0]
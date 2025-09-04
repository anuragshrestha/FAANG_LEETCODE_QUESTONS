"""
540. Single Element in a Sorted Array
Company: Google
Problem Link: https://leetcode.com/problems/single-element-in-a-sorted-array/description/
"""


class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        #initialize left = 0, right = n - 1
        #loop until left <= last
        #find mid : (left + right) // 2
        #check if both the left and right side of mid is different. If so
        #then return the value at mid index.
        #elif: if the mid and mid - 1 value is same. then check if
        #mid -1 is even and mid is odd. if so move the mid to mid + 1
        #else: move mid to mid - 1
        #else if mid and mid + 1 is same then check the same edge case.
        #return -1 at the end

        n = len(nums) 
        left, right = 0, n - 1

        while left <= right:
           
            mid = (left + right) // 2
            prev = None 
            nex = None
            cur = nums[mid]

            if mid > 0:
                prev = nums[mid - 1]
            
            if mid < n - 1:
                nex = nums[mid + 1]

            if cur != prev and cur != nex:
                return cur
            elif cur == prev:
                if mid % 2 == 1:
                    left = mid + 1
                else:
                    right = mid - 1
            else:
                if mid % 2 == 0:
                    left = mid + 1
                else:
                    print(4)
                    right = mid - 1

        
        return -1

            

        
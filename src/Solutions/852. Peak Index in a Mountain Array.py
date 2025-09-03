## 852. Peak Index in a Mountain Array `https://leetcode.com/problems/peak-index-in-a-mountain-array/description/`

"""""
 - Solution:

 class Solution(object):
    def peakIndexInMountainArray(self, arr):
        
        :type arr: List[int]
        :rtype: int
        
        
        #initialize first, last = 1, n - 2
        #loop until first <= last
        #find mid = first + last // 2
        #check if mid > mid - 1 and mid > mid + 1
        #if so return mid
        #elif mid < mid - 1, move last = mid - 1
        #else first = mid + 1
        #return -1 at the end
       
        n = len(arr) 
        first = 1
        last = n - 2

        while first <= last:
            mid = (first + last) // 2
            
            prev = arr[mid - 1]
            nex = arr[mid + 1]
            cur = arr[mid]

            if prev < cur > nex:
                return mid
            elif prev > cur:
                last = mid - 1
            else:
                first = mid + 1
        

        return -1
        
"""""
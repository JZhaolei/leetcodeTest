class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        low = 0
        high = len(nums) - 1
        mid = (high + low) / 2
        while high - low > 1:
            count = 0
            for k in nums:
                if mid < k <= high:
                    count += 1
            if count > high - mid:
                low = mid
            else:
                high = mid
            mid = (high + low) / 2
        return high

class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        low = 0
        high = len(nums) - 1
        mid = (high + low) / 2
        while high-low>1:
            if low<= nums[mid]<=mid:
                 high=mid
            if high>=nums[mid]>mid:
                low =mid
            mid = (low + high)/2
        return high
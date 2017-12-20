class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        n=nums.count(target)
        if n==0:
            return [-1,-1]
        else:
            for i in range(len(nums)):
                if nums[i]==target:
                    return [i,i+n-1]
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        if not nums1 and not nums2:
            return []
        nums=nums1+nums2
        nums.sort()
        n=len(nums)
        if n==1:
            median = nums[0]
        elif n%2==0:
            median = (float(nums[(n-1)/2])+float(nums[(n+1)/2]))/2
        else:
            median = float(nums[n/2])
        return median


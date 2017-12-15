class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums==[]:
            return 0
        else:
            myset=set(nums)
            for i in myset:
                q = nums.count(i)
                if q > len(nums)/2:
                    return i

        return sorted(nums)[len(nums)/2] #¸üÓÅ
#�ҵķ���
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for num in nums:
            if nums.count(num)==1:
                return num

#��
def singleNumber3(self, nums):
    return 2*sum(set(nums))-sum(nums)
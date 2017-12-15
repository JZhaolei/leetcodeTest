class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        ##arr=[]
       # for i in range(len(nums)):
       #     for j in range(i+1,len(nums)):
       #         answer = nums[i]+nums[j]
       #         if answer - target == 0:
       #             arr=[i,j]
       #             #arr.append([i, j])
       #             #arr=list(arr)
       # return arr
        if len(nums) <= 1:
            return False
        buff_dict = {}
        for i in range(len(nums)):
            if nums[i] in buff_dict:
                return [buff_dict[nums[i]], i]
            else:
                buff_dict[target - nums[i]] = i
                
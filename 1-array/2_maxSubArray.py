class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
       
       """
       
      #  maxSum=0
      #  max_dict={}
       # for i in range(1,len(nums)+1):
        #    for j in range(len(nums)-i+1):
         #       sli=tuple(nums[j:j+i])
          #      max_dict[sli] = sum(nums[j:j+i])
           #     maxkey = max(max_dict)
            #    maxSum = max_dict[maxkey]
             #   #maxSum=max(sum(nums[j:j+i]))
       # return maxSum
      
        if not nums:
            return 0
        curSum = maxSum = nums[0]
        for num in nums[1:]:
            curSum = max(num, curSum + num)
            maxSum = max(maxSum, curSum)

        return maxSum   
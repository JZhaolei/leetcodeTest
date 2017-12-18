#ÎÒµÄ
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        S=[]
        for j in range(len(height)):
            for i in range(j,len(height)):
                s = (min(height[j], height[i]))*abs(j-i)
                S.append(s)
                maxs = max(S)
        return maxs

#´ð°¸
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        res, l, r = 0, 0, len(height) - 1
        while l < r:
            h = min(height[l], height[r])
            res, l, r = max(res,  h * (r - l)), l + (height[l] == h), r - (height[r] == h)
        return res
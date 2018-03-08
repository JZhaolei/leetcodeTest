#思路一
class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        ans = 0
        for i in range(1,len(height)):
            left_max=0
            right_max=0
            for j in range(0,i+1):
                left_max=max(left_max,height[j])
            for j in range(i,len(height)):
                right_max=max(right_max,height[j])
            ans += min(left_max,right_max)-height[i]
        return ans

#思路二
class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        ans = 0
        if not height:
            return 0
        left_max=[]
        right_max =[]
        for i in range(0,len(height)):
            left_max.append(0)
            right_max.append(0)
        
        left_max[0]=height[0]
        for i in range(1,len(height)):
            left_max[i]=max(height[i], left_max[i - 1])
            
        right_max[len(height)-1] = height[len(height)-1]
        for i in range(len(height)-2,-1,-1):#len(height)-2到0倒着取
            right_max[i]=max(height[i], right_max[i + 1])
            
        for i in range(1,len(height)-1):
            ans += min(left_max[i],right_max[i])-height[i]
        return ans

#思路三
class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        ans = 0
        left = 0
        right = len(height)-1
        left_max = 0
        right_max = 0
        if not height:
            return 0
        while left<right:
            if height[left]<height[right]:
                if height[left]>=left_max:
                    left_max=height[left]
                ans += left_max - height[left]
                left+=1
            else:
                if height[right]>=right_max:
                    right_max=height[right]
                ans += right_max - height[right]
                right -=1
        return ans
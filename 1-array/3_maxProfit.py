class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_profit, min_price = 0, float('inf') #引入正无穷，为了初始化min，使输入数字可以替代它
        for price in prices:
            min_price = min(min_price, price) #最小买入价格
            profit = price - min_price   #令price即为卖出价格，定了min_price后就相当于只找他后边的卖出价格的最大值
            max_profit = max(max_profit, profit)
        return max_profit
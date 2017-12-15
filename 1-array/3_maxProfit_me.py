class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices)<2: #考虑输入为空情况
            return 0
        
        else:
            buymin = prices[0] #初始化输入
            sellmax = 0
            maxprofit = []
            Maxprofit = 0
            for buy in prices[1:]:  
                buymin = min(buymin, buy) #从buy后开始寻找最小的买入
                if prices[prices.index(buymin)+1:]==[]: #从买入后寻找最大的卖出，若没有值了置0，把多次循环所得的maxprofit放在一个数组，取最值
                    maxprofit.append(0)
                else:
                    sellmax = max(prices[prices.index(buymin)+1:])
                    if sellmax < buymin:
                        maxprofit.append(0)
                    else:   
                        m = sellmax-buymin
                        maxprofit.append(m)
                Maxprofit = max(maxprofit)
        return Maxprofit
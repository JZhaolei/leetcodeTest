class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices)<2: #��������Ϊ�����
            return 0
        
        else:
            buymin = prices[0] #��ʼ������
            sellmax = 0
            maxprofit = []
            Maxprofit = 0
            for buy in prices[1:]:  
                buymin = min(buymin, buy) #��buy��ʼѰ����С������
                if prices[prices.index(buymin)+1:]==[]: #�������Ѱ��������������û��ֵ����0���Ѷ��ѭ�����õ�maxprofit����һ�����飬ȡ��ֵ
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
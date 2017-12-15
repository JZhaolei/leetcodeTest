class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_profit, min_price = 0, float('inf') #���������Ϊ�˳�ʼ��min��ʹ�������ֿ��������
        for price in prices:
            min_price = min(min_price, price) #��С����۸�
            profit = price - min_price   #��price��Ϊ�����۸񣬶���min_price����൱��ֻ������ߵ������۸�����ֵ
            max_profit = max(max_profit, profit)
        return max_profit
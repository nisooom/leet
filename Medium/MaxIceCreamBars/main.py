class Solution(object):
    def maxIceCream(self, costs, coins):
        """
        :type costs: List[int]
        :type coins: int
        :rtype: int
        """
        icecreamsbought = 0
        costs.sort()
        for i in range(len(costs)):
            if coins == 0: return icecreamsbought
            if costs[i] > coins:
                pass
            else:
                coins -= costs[i]
                icecreamsbought += 1

        return icecreamsbought

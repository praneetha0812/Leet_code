class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # Initialize variables
        min_price = float('inf')
        max_profit = 0
        
        # Loop through each price
        for price in prices:
            # Update min_price with the lowest value so far
            min_price = min(min_price, price)
            # Calculate the current profit and update max_profit if it's larger
            max_profit = max(max_profit, price - min_price)
        
        return max_profit

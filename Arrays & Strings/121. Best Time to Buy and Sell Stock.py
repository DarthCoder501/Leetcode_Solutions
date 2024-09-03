class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Initialize min_value to the first price in the array
        # This tracks the lowest price encountered so far
        min_value = prices[0]
        
        # Initialize max_profit to 0
        # This will hold the maximum profit possible
        max_profit = 0
        
        # Loop through each price in the prices array
        for i in range(len(prices)):
            # If the current price is lower than the minimum value found so far
            # Update min_value to be this new lower price
            if prices[i] < min_value:
                min_value = prices[i]
            
            # If selling at the current price would yield a higher profit
            # than any profit found so far, update max_profit
            elif prices[i] - min_value > max_profit: 
                max_profit = prices[i] - min_value
        
        # Return the maximum profit found
        return max_profit

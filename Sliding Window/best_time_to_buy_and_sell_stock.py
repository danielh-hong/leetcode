# 121. Best Time to Buy and Sell Stock (easy)
# Sliding window
'''
You are given an array prices where prices[i] is the price of a given stock on the ith day.
You want to maximize your profit by choosing a single day to buy one stock and choosing 
a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. 
If you cannot achieve any profit, return 0.

Example 1:
Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
Example 2:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.
'''

# [7,6,4,3,1]
# [7,1,5,3,6,4]
# [3,1,5,0,6,4]
# Good solution:
# Brainstorm:
# Two pointer (sliding window) question
# Want to make left pointer be smallest and right pointer be biggest
# So start with L = R = 0
# R always >= L
# If current date being checked is < current left pointer date, L += 1 (loop this)
# * NOTE again, right pointer has to be moved with left pointer when necessar since R >= L
# If current date being checked is > than right pointer, R += 1 (loop this)
# Store max
# ... maybe always moving right pointer works?

# done by self
def maxProfit(prices):
    n = len(prices)
    max_profit = 0
    left = 0
    for right in range(len(prices)):
        # we only want left to point to values that are smaller than the current left
        # When prices[right] < prices[left] then its a smaller value so we go to it
        # with the while loop
        while left < right and prices[right] < prices[left]: 
            left += 1
            max_profit = max(max_profit, prices[right] - prices[left])
        max_profit = max(max_profit, prices[right] - prices[left])
    print(max_profit)
    return(max_profit)

maxProfit([7,6,4,3,1])
maxProfit([7,1,5,3,6,4])
maxProfit([3,1,5,0,6,4])






# BAD O(n^2) brute force solution:
def maxProfitBad(prices):
    n = len(prices)
    max_profit = 0
    
    for i in range(n - 1):  # till second last day
        for j in range(i + 1, n):  # Compare with all future days
            profit = prices[j] - prices[i]  # Calculate profit
            if profit > max_profit:
                max_profit = profit  # Update max profit
    
    return max_profit
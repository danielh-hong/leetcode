# 746. Min Cost Climbing Stairs

'''
You are given an integer array cost where cost[i] is the 
cost of ith step on a staircase. Once you pay the cost, 
you can either climb one or two steps.

You can either start from the step with index 0, or 
the step with index 1.

Return the minimum cost to reach the top of the floor.

Example 1:

Input: cost = [10,15,20]
Output: 15
Explanation: You will start at index 1.
- Pay 15 and climb two steps to reach the top.
The total cost is 15.
Example 2:

Input: cost = [1,100,1,1,1,100,1,1,100,1]
Output: 6
Explanation: You will start at index 0.
- Pay 1 and climb two steps to reach index 2.
- Pay 1 and climb two steps to reach index 4.
- Pay 1 and climb two steps to reach index 6.
- Pay 1 and climb one step to reach index 7.
- Pay 1 and climb two steps to reach index 9.
- Pay 1 and climb one step to reach the top.
The total cost is 6.
'''

# Use dynamic programming approach. Can either reach 
# from n - 2 cost + current cost or from n - 1 cost + current cost.
# then set current cost to the cheaper option checking between those two
# O(1) space with O(n) time complexity
def minCostClimbingStairs(cost):
    c1 = cost[0]
    c2 = cost[1]

    if len(cost) == 2:
        return min(c1, c2)

    for i in range(2, len(cost) - 1):
        temp = c2
        c2 = min(c1, c2) + cost[i]
        c1 = temp

    return min(c2, c1 + cost[-1])


# Try going cheapest & longest path backwards DOESNT WORK!!!
# Greedy strategy doesn't work in this case.
def minCostClimbingStairsBroken(cost):
    if len(cost) == 1:
        return cost[0]
    if len(cost) == 2:
        return min(cost[0], cost[1])
    
    min_cost = 0
    p = len(cost)
    while p - 1 > 0:
        if cost[p-2] <= cost[p-1]:
            min_cost += cost[p-2]
            p -= 2
        else:
            min_cost += cost[p-1]
            p -= 1
          
    min_cost2 = 0
    p = -1
    while p < len(cost) - 2:
        if cost[p + 2] <= cost[p + 1]:
            min_cost2 += cost[p + 2]
            p += 2
        else:
            min_cost2 += cost[p + 1]
            p += 1

        print("test")

    return min(min_cost2, min_cost)
  

        
        
  
[1,100,0,1,1,2]
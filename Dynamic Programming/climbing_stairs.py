# 70. Climbing Stairs. Easy problem.

'''
70. Climbing Stairs

You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
'''

checked = {}

# This is O(n). Unoptimized it is O(2^n)
def climbStairs(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n in checked:
        return checked[n]
    
    checked[n] = climbStairs(n-1) + climbStairs(n-2)  # Store computed value
    return checked[n]

# Alternatively




def climbStairsLoop(n):
    s1 = 1
    s2 = 2

    return 1 if n == 1 else None

    for i in range(3, n+1):
        temp = s2
        s2 = s2 + s1
        s1 = temp

    return 
# 334. Increasing Triplet Subsequence (Medium)
'''
Given an integer array nums, return true if there exists 
a triple of indices (i, j, k) such that i < j < k and
nums[i] < nums[j] < nums[k]. If no such indices exists, return false.
'''

'''
Example 1:

Input: nums = [1,2,3,4,5]
Output: true
Explanation: Any triplet where i < j < k is valid.
Example 2:

Input: nums = [5,4,3,2,1]
Output: false
Explanation: No triplet exists.
Example 3:

Input: nums = [2,1,5,0,4,6]
Output: true
Explanation: The triplet (3, 4, 5) is valid because nums[3] == 0 < nums[4] == 4 < nums[5] == 6.
'''

# Search this up but i understand it. It's a greedy algorithm.
class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # crucial point is that while iterating, the values of first 
        # and second are updated only if we find smaller values, making 
        # the algorithm efficient in identifying the increasing sequence.

        first = nums[0]
        second = float('inf') # need tis to be inf can't be nums[0] or error
        for num in nums:
            if num <= first: # <= necessary or else the else statemnt won't work since has to eb bigger
                first = num
            elif num <= second: 
                second = num
            else:
                return True
        return False
    
# Time Complexity: 
# O(n), since we iterate through the list once.
# Space Complexity: 
# O(1), as we only use two extra variables.

'''
"greedy algorithm" applies to this approach because it makes locally optimal choices at each step in hopes of finding the globally optimal solution (i.e., identifying an increasing triplet).

Characteristics of Greedy Algorithms in This Context:
No backtracking:
Once an element is assigned to first or second, it doesn't revisit earlier elements to reconsider.

Optimal substructure:
The problem can be broken down into smaller subproblems (finding smaller elements), and solving these optimally contributes to the larger solution.

Fast decision-making:
The algorithm makes decisions at each step without postponing or revisiting previous states, allowing it to run in 

O(n) time.
'''


# WORSE SOLUTION (O(n) still though). Using DP
def increasingTriplet(nums):
    n = len(nums)
    if n < 3:
        return False

    left_min = [0] * n
    right_max = [0] * n

    # Compute the minimum values from the left side
    left_min[0] = nums[0]
    for i in range(1, n):
        left_min[i] = min(left_min[i - 1], nums[i])

    # Compute the maximum values from the right side
    right_max[-1] = nums[-1]
    for i in range(n - 2, -1, -1):
        right_max[i] = max(right_max[i + 1], nums[i])

    # Check for an increasing triplet
    for j in range(1, n - 1):
        if left_min[j - 1] < nums[j] < right_max[j + 1]:
            return True

    return False

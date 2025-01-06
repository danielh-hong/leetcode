# Easy (Completed)
'''
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
'''

# Time: O(n^2):
nums = [2, 7, 11, 15]
target = 9

def two_sum(nums, target):
  for i in range(len(nums)):
    for j in range(i+1, len(nums)): # no index out of range error
      if (nums[i] + nums[j] == target):
        print([i,j])
        return [i, j]
      
two_sum(nums, target)

# Time: O(n)
def two_sum_hashmap(nums, target):
  seen_nums = {} # num, index
  for i in range(len(nums)): # O(n) 
    complement = target - nums[i]
    if complement in seen_nums: # automatically does it by key
      print([i, seen_nums[complement]])
      return [i, seen_nums[complement]]
    seen_nums[nums[i]] = i

two_sum_hashmap(nums, target)
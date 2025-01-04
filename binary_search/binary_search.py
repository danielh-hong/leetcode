# 704. Binary Search
# Leetcode Easy Problem

'''
Given an array of integers nums which is sorted in ascending order, 
and an integer target, write a function to search target in nums. 
If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.

Example 1:

Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4
Example 2:

Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1
'''
# Strategy: 
# Check if target above middle num (O(1) to access since we're just using pointer arithmetic)
# If above, search top half
# If below, search bottom half
# Repeat

def search(nums, target):
  left = 0
  right = len(nums) - 1
  while right - left > 1: # Figure out proper case after, probably something with like right - left > 1
    # Note: int floors a float
    middle_index = left + int((right - left) / 2)
    
    if target > nums[middle_index]:
      left = middle_index + 1

    elif target < nums[middle_index]:
      right = middle_index - 1

    else:
      return middle_index 

  # if less than or equal to 1:
  if target == nums[left]:
    return left
  elif target == nums[right]:
    return right
  return -1

[1, 2]
def search_better(nums, target):
    left = 0
    right = len(nums) - 1
    
    while left <= right:
        middle_index = left + (right - left) // 2 # // is floor division
        
        if nums[middle_index] == target:
            return middle_index
        elif nums[middle_index] < target:
            left = middle_index + 1
        else:
            right = middle_index - 1
    
    return -1
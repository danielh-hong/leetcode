# 167. Two Sum II - Input Array Is Sorted
# Medium, Two Pointers COMPLETED (completed)

# Given a 1-indexed array of integers numbers that is already 
# sorted in non-decreasing order, find two numbers such that they 
# add up to a specific target number. Let these two numbers be 
# numbers[index1] and numbers[index2] 
# where 1 <= index1 < index2 <= numbers.length.

# Return the indices of the two numbers, index1 and index2, 
# added by one as an integer array [index1, index2] of length 2.

# The tests are generated such that there is exactly one solution. 
# You may not use the same element twice.

# Your solution must use only constant extra space.


# Example 1:
# Input: numbers = [2,7,11,15], target = 9
# Output: [1,2]
# Explanation: The sum of 2 and 7 is 9. Therefore, 
# index1 = 1, index2 = 2. We return [1, 2].

# Example 2:
# Input: numbers = [2,3,4], target = 6
# Output: [1,3]
# Explanation: The sum of 2 and 4 is 6. Therefore 
# index1 = 1, index2 = 3. We return [1, 3].

# Example 3:
# Input: numbers = [-1,0], target = -1
# Output: [1,2]
# Explanation: The sum of -1 and 0 is -1. 
# Therefore index1 = 1, index2 = 2. We return [1, 2].



# Good solution (using two pointer method, using the fact that array is sorted):
'''
Given the constraints that the input array is sorted and there is exactly one solution, 
we can use the two-pointer technique to solve this problem efficiently in 
O(n) time with O(1) space.

Steps
Initialize two pointers:

left starting at index 0 (the first element of the array).
right starting at index numbers.length - 1 (the last element of the array).
While left < right:

Calculate the sum of the numbers at the left and right pointers: currentSum = numbers[left] + numbers[right].
If currentSum equals the target, return [left + 1, right + 1] (convert to 1-based indexing).
If currentSum < target, increment the left pointer (move to a larger value).
If currentSum > target, decrement the right pointer (move to a smaller value).
Since the problem guarantees exactly one solution, no additional checks are required.
'''

# Below solution is good solution with O(1) space & O(n) time complexity
# Must be solution so just use while True:
def twoSumGood(numbers, target):
    left = 0
    right = len(numbers) - 1
    while True: # O(n) iterating through
        if numbers[left] + numbers[right] == target:
            return [left+1, right+1]
        elif target > numbers[left] + numbers[right]:
            left += 1
        else:
            right -= 1

# Bad solution (Not using two pointers):
def twoSum(numbers, target):
    """
    :type numbers: List[int]
    :type target: int
    :rtype: List[int]
    """
    seen_nums = {} # dict, num, index (1-index)
    for i in range(len(numbers)): # O(n)
        complement = target - numbers[i] # O(1)
        if complement in seen_nums: # O(1) lookup
            return [seen_nums[complement], i+1]
        else:
            seen_nums[numbers[i]] = i+1
    return False

    
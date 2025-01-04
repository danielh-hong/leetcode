# Contains Duplicates 217
'''Given an integer array nums, return true if any value appears 
at least twice in the array, and return false if every element is 
distinct.

Example 1:

Input: nums = [1,2,3,1]
Output: true

Explanation:
The element 1 occurs at the indices 0 and 3.

Example 2:
Input: nums = [1,2,3,4]
Output: false

Explanation:
All elements are distinct.

Example 3:
Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true
'''

# NOTE: lookup in list is O(n)!

# O(n) solutoin using hashmap; Note that I believe you can do this with a set:
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # Iterate through list (O(n)), adding everything to hashmap
        # Note that list would be O(n^2) since searching in list is O(n)
        # But if we use hashmap it's only O(n)

        checked_nums = {}
        for num in nums:
            if num in checked_nums:
                return True
            checked_nums[num] = 1 # 1 is basically a random # we don't really even need it
        return False
    

# Better solution (using set), since don't need key-value pairs:
def containsDuplicateSet(nums):
    checked_nums = set()
    for num in nums:
        if num in checked_nums:
            return True
        checked_nums.add(num)
    return False    

def containsDuplicateSet2(nums):
    if len(nums) != len(set(nums)): # set(nums) is probably O(n) & comparison is O(1) so O(n)
        return True
    return False
    

# Brute force solution: O(n^2)
def containsDuplicateBrute(self, nums):
    n = len(nums)
    for i in range(n - 1):
        for j in range(i + 1, n):
            if nums[i] == nums[j]:
                return True
    return False
          

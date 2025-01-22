# Product of Array Except Self
# First Try
# Medium
'''
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

 

Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
'''


# O(n) idea with no division:
# iterate the list through once, making a new list where each item is the multiplication of all items to the left
# iteraet the list (right to left now), making a new list where each item is teh multiplication of all items to the right
# iterate through the original list one more time, multiplying left side from l1 and right side from l2 for the actual multiplication

# FIRST TRY!!
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        l = [nums[0]] * len(nums)
        r = [nums[-1]] * len(nums)
        ret = [0] * len(nums)
        for i in range(1, len(nums) - 1):
            l[i] = nums[i] * l[i - 1]

        for i in range(len(nums) - 2, 0, -1):
            r[i] = nums[i] * r[i + 1]

        ret[0] = r[1]
        ret[-1] = l[-2]
        for i in range(1, len(nums) - 1):
            ret[i] = l[i-1] * r[i+1]

        return ret
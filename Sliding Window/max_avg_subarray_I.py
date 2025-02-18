# 643. Maximum Average Subarray I

'''
You are given an integer array nums consisting of n elements, and an integer k.

Find a contiguous subarray whose length is equal to k that has 
the maximum average value and return this value. Any answer with 
a calculation error less than 10-5 will be accepted.

Example 1:

Input: nums = [1,12,-5,-6,50,3], k = 4
Output: 12.75000
Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75
Example 2:

Input: nums = [5], k = 1
Output: 5.00000
'''
class Solution:
    def findMaxAverage(self, nums, k):
        sum_ = sum(nums[0:k])
        max_avg = sum_ / k

        for i in range(1, len(nums) - k + 1):
            sum_ = sum_ + nums[i + k - 1] - nums[i - 1]
            max_avg = max(max_avg, sum_/k)

        return max_avg


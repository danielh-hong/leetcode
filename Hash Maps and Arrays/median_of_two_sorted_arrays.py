# 4. Median of Two Sorted Arrays (hard), Arrays

'''
Given two sorted arrays nums1 and nums2 of size m and n respectively, 
return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

 

Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
Example 2:

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
'''
# Bad O(n) solution:
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        # merge the two arrays then access middle
        new_arr = []
        p1 = 0
        p2 = 0
        while p1 < len(nums1) and p2 < len(nums2):
            if nums1[p1] < nums2[p2]:
                new_arr.append(nums1[p1])
                p1 += 1
            else:
                new_arr.append(nums2[p2])
                p2 += 1
        if p1 == len(nums1):
            new_arr = new_arr + nums2[p2:len(nums2)]
        elif p2 == len(nums2):
            new_arr = new_arr + nums1[p1:len(nums1)]
        print(new_arr)
        if len(new_arr) % 2 == 1:
            return new_arr[len(new_arr) // 2]

        return float(new_arr[len(new_arr) // 2 - 1] + new_arr[len(new_arr) // 2]) / 2 # Note this float is necessary, but not necessary in python3
    # python 2: Integer division (/) between two integers results in an integer.
    # python 3: Python 3.x: the / operator always performs floating-point division, even if both operands are integers.
        

'''
Approach 1: Merge and Sort
Create a new array with a size equal to the total number of elements in both input arrays.
Insert elements from both input arrays into the new array.
Sort the new array.
Find and return the median of the sorted array.
Time Complexity

In the worst case TC is O((n + m) * log(n + m)).
Space Complexity

O(n + m), where ‘n’ and ‘m’ are the sizes of the arrays.
'''

'''
Approach 2: Two-Pointer Method
Initialize two pointers, i and j, both initially set to 0.
Move the pointer that corresponds to the smaller value forward at each step.
Continue moving the pointers until you have processed half of the total number of elements.
Calculate and return the median based on the values pointed to by i and j.
Time Complexity

O(n + m), where ‘n’ & ‘m’ are the sizes of the two arrays.
Space Complexity

O(1).
'''

'''
Approach 3: Binary Search
Use binary search to partition the smaller of the two input arrays into two parts.
Find the partition of the larger array such that the sum of elements on the left side of the partition in both arrays is half of the total elements.
Check if this partition is valid by verifying if the largest number on the left side is smaller than the smallest number on the right side.
If the partition is valid, calculate and return the median.
Time Complexity

O(logm/logn)
Space Complexity

O(1)
'''

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        # Make sure nums1 is smaller - makes binary search more efficient
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        x, y = len(nums1), len(nums2)  # lengths of arrays
        start, end = 0, x  # binary search range for first array

        while start <= end:
            # Try splitting first array at middle
            partX = (start + end) // 2  
            # Calculate where to split second array to get equal halves
            # Example: if arrays are [1,2] and [3,4]
            # partX = 1 means split first array: [1 | 2]
            # partY = 2 means split second array: [3 | 4]
            partY = (x + y + 1) // 2 - partX

            # Get values around partition points
            # For [1|2] and [3|4]:
            # leftX = 1, rightX = 2
            # leftY = 3, rightY = 4
            leftX = float('-inf') if partX == 0 else nums1[partX - 1]
            rightX = float('inf') if partX == x else nums1[partX]
            leftY = float('-inf') if partY == 0 else nums2[partY - 1]
            rightY = float('inf') if partY == y else nums2[partY]

            # Check if this split is valid (left sides <= right sides)
            if leftX <= rightY and leftY <= rightX:
                # If odd total length, median is max of left sides
                if (x + y) % 2 != 0:
                    return max(leftX, leftY)
                # If even length, median is average of max(left) and min(right)
                # For [1|2] [3|4]: (max(1,3) + min(2,4))/2 = (3+2)/2 = 2.5
                return (max(leftX, leftY) + min(rightX, rightY)) / 2.0
            # If split is wrong, adjust binary search
            elif leftX > rightY:  # left side too big
                end = partX - 1
            else:  # left side too small
                start = partX + 1

        return 0.0
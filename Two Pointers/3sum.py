'''
Given an integer array nums, return all the triplets 
[nums[i], nums[j], nums[k]] such that i != j, i != k, and 
j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.
Example 2:

Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.
Example 3:

Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.
 

Constraints:

3 <= nums.length <= 3000
-105 <= nums[i] <= 105
'''

# had to work hard for this omg i'm so stupid
# better solution without post processing (helped by chat):
def threeSumBetter(nums):
    sorted_n = sorted(nums)

    ret = []

    for l in range(len(nums) - 2): # to 3 before end
        m = l + 1
        r = len(nums) - 1

        if l >= 1 and sorted_n[l] == sorted_n[l-1]:
            continue

        while m < r:
            s = sorted_n[l] + sorted_n[m] + sorted_n[r]
            if s == 0:
                ret.append([sorted_n[l], sorted_n[m], sorted_n[r]])
                m += 1
                r -= 1

                while sorted_n[r] == sorted_n[r + 1] and r >= 2:
                    r -= 1
                while sorted_n[m] == sorted_n[m - 1] and m <= len(nums) - 3:
                    m += 1
            elif s > 0:
                r -= 1
            else:
                m += 1
                

    return ret
      
    seen = set()
    ret_final = []
    # should already be sorted
    for three_nums in ret:
        encoded_str = ''.join(str(num) for num in three_nums)
        if encoded_str not in seen:
            ret_final.append(three_nums)
            seen.add(encoded_str)
            
    return ret_final

# descent Solution I thought of myself with hint: (basically one of the things iterates through, and other uses two pointer soln)
def threeSum(nums):
    sorted_n = sorted(nums)
    # [-4, -1, -1, 0, 1, 2]
    #   l   m            r
    #   nums[m] + nums[r] have to equal abs(nums[l])
    #   inner while loop should go on while m < r then l incremeents and m resets to l + m
    ret = []

    for l in range(len(nums) - 2): # to 3 before end
        m = l + 1
        r = len(nums) - 1

        while m < r:
            s = sorted_n[l] + sorted_n[m] + sorted_n[r]
            if s == 0:
                ret.append([sorted_n[l], sorted_n[m], sorted_n[r]])
                r -= 1
                m += 1
            if s > 0:
                r -= 1
            if s < 0:
                m += 1
      
    seen = set()
    ret_final = []
    # should already be sorted
    for three_nums in ret:
        encoded_str = ''.join(str(num) for num in three_nums)
        if encoded_str not in seen:
            ret_final.append(three_nums)
            seen.add(encoded_str)
            
    return ret_final
threeSum([-1,0,1,2,-1,-4])

# O(n^2) sort of
# l start at 0, r start at end
# m moves, then shift l / r accordingly ONCE

# Below would've been good if i finished i think... but i had the wrong idea
def threeSumWouldHaveBeen(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    sorted_nums = sorted(nums) # O(n log n) sort - I think necessary, sorted always returns list
    l = 0
    r = len(nums) - 1
    m = (len(nums) - 1) // 2

    while l < r:
        while l + m + r > 0:
            if m - 1 != l:
                m -= 1
            pass
        pass
            
            

# Works but shit and timed out
def threeSum(nums):                  
    # bad, shit brute force method: (O(n^3))
    num_to_let = {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e', 6: 'f', 7: 'g', 8: 'h', 9: 'i', 0: 'j'} # O(1) since size is constant

    ret1 = []
    # O(n^3)
    for i in range(len(nums) - 2):
        for j in range(i+1, len(nums) - 1):
            for k in range(j+1, len(nums)):
                if nums[i] + nums[j] + nums[k] == 0:
                    ret1.append([nums[i], nums[j], nums[k]])

    # unecessary can just check if list exists lol, maybe slightly beneficial
    exists = set()
    ret2 = []
    print(ret1)
    for lis in ret1:
        sorted_lis = sorted(lis) # O(m * k log k), where k is length of each triplet and m is size of ret1
        hashed_str = ''.join(str(num) for num in sorted_lis)
        if hashed_str not in exists: # O(m) check
            exists.add(hashed_str)
            ret2.append(lis) # O(m) append
    
      
                    
    return ret2
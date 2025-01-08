# Top K Frequenet Element
# Hash map / Array question
# Medium Difficulty

'''
347. Top K Frequent Elements
'''

'''
Given an integer array nums and an integer k, return the k most 
frequent elements. You may return the answer in any order.
'''

# Time Complexity breakdown:
'''
- Counting frequencies with dictionary: O(n)
- Converting dict to list: O(n)
- Sorting the list: O(n log n)
- Final loop to get k elements: O(k)

Total: O(n log n)
'''

# Decent ish solution (O(n log n))
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # O(n log n + n) solution:
        most_freq = []
        seen_nums = {}
        for i in range(len(nums)): # O(n)
            if nums[i] in seen_nums:
                seen_nums[nums[i]] += 1
            else:
                seen_nums[nums[i]] = 1

        # now find the k most frequent elements (the k highest values)

        lis_conversion = list(seen_nums.items()) # O(n) probably, has to iterate through dic

        # lambda arguments: expression
        # arguments: A comma-separated list of parameters (just like in a regular function).
        # expression: A single expression (the result of this expression is automatically returned).

        lis_conversion.sort(key=lambda x: x[1], reverse=True) # O(n log n)

        final_ret = []
        for i in range(k): # shit solution
            final_ret.append(lis_conversion[i][0])

        return final_ret
    



# dic = {"a": 1, "b": 2, "c": 3}
# print(dic)
# print(list(dic.items()))
            


        
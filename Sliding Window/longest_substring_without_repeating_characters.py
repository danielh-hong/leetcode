'''
Given a string s, find the length of the longest 
substring
 without repeating characters.

 

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
'''

# better solution O(n)
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        seen = set()
        l = 0
        max_length = 0

        for r in range(len(s)):
            while s[r] in seen:
                seen.remove(s[l])
                l += 1
            seen.add(s[r])
            max_length = max(max_length, r - l + 1)

        return max_length

# ^
'''
Sliding Window:

Maintain a window of unique characters using two pointers (l and r).
Move the right pointer r to expand the window.
If a character is already in the seen set, move the left pointer l until the character is removed from the set.
Efficiency:

Each character is added to and removed from the set at most once, resulting in O(n) time complexity.
Space complexity is O(min(n,a)), where a is the size of the character set (e.g., 26 for 
lowercase English letters).

Clean and Concise:
The logic avoids unnecessary calls to is_unique, and the code is more straightforward and efficient.

'''
# My solution worst case O(n^2)
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        def is_unique(s):
            seen = set()
            for char in s:
                if char in seen:
                    return False
                seen.add(char)
            return True

        l = 0
        r = 1
        while r <= len(s):
            if is_unique(s[l:r]):
                r += 1
                continue
            l += 1
            r += 1

        return r - l - 1


        


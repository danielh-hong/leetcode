# 345. Reverse Vowels of a String (easy) (complete)
'''
Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in 
both lower and upper cases, more than once.
 
Example 1:

Input: s = "IceCreAm"

Output: "AceCreIm"

Explanation:

The vowels in s are ['I', 'e', 'e', 'A']. On reversing the vowels, s becomes "AceCreIm".

Example 2:

Input: s = "leetcode"

Output: "leotcede"

 

Constraints:

1 <= s.length <= 3 * 105
s consist of printable ASCII characters.
'''

# own solution. Note that need to convert to list since string is immutable.
class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        s_list = list(s)
        # set of vowels:
        vowels = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}
        l = 0
        r = len(s) - 1
        while l < r:
            while s[l] not in vowels and l < r:
                l += 1
            while s[r] not in vowels and l < r:
                r -= 1
            if s[l] in vowels and s[r] in vowels:
                s_list[l], s_list[r] = s_list[r], s_list[l]
                l += 1
                r -= 1
        return "".join(s_list)
                

s = "abcde"
s[0] = "e"
print(s)
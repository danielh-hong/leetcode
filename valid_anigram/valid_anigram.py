# 242. Valid Anagram
'''
An anagram is a word or phrase formed by rearranging the 
letters of a different word or phrase, using all the original 
letters exactly once.

Given two strings s and t, return true if t is an 
anagram of s, and false otherwise.

Example 1:
Input: s = "anagram", t = "nagaram"
Output: true

Example 2:
Input: s = "rat", t = "car"
Output: false

Constraints:

1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.
 
Follow up: What if the inputs contain Unicode characters? 
How would you adapt your solution to such a case?
'''

# Note that len("string") is O(1), because the data structures
# save the size as an attribute.
# if it weren't saved it would be O(n). Attribute is 
# a property associated with an object, and are accessed
# using dot notation. Objects are instances of a class.

def isAnagram(s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    # my solution (sub optimal): 
    # iterate through s & create dictionary O(n)
    # iterate through t & create dictionary O(m)
    # check if dictionaries are equal O(n)
    s_char_and_frequency = {}
    t_char_and_frequency = {}
    for i in range(len(s)):
      if s[i] not in s_char_and_frequency: # this is already O(k) where k is length of keys
         s_char_and_frequency[s[i]] = 1
      else:
         s_char_and_frequency[s[i]] += 1
    
    for i in range(len(t)):
      if t[i] not in t_char_and_frequency: # this is already O(k) where k is length of keys
         t_char_and_frequency[t[i]] = 1
      else:
         t_char_and_frequency[t[i]] += 1

    return True if (s_char_and_frequency == t_char_and_frequency) else False
        
        

    # Note that the below doesn't work, for example,
    # aacc and aaac would return True
    # return True if (len(s) == len(t) and set(s) == set(t)) else False
    
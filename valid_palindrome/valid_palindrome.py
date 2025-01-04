# Easy, 125. Valid Palindrome (2 pointer)

'''
A phrase is a palindrome if, after converting all uppercase letters 
into lowercase letters and removing all non-alphanumeric characters, 
it reads the same forward and backward. Alphanumeric characters include 
letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

Example 1:
Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.

Example 2:
Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
Example 3:

Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.
'''

print('a', ord('a'))
print('A', ord('A'))
print('z', ord('z'))
print('Z', ord('Z'))
print(chr(90))
print(1, ord('1'))
print(0, ord('0'))
print(9, ord('9'))


def isPalindrome(s):
  """
  :type s: str
  :rtype: bool
  """
  letters = set()
  for i in range(65, 91):
    letters.add(chr(i))
    letters.add(chr(i+32))

  for i in range(48, 58):
    letters.add(chr(i))

  # aa
  # i for start pointer, j for end pointer
  z = len(s)
  i = 0
  j = z-1

  while i <= j:
    if s[i] not in letters: # should be O(1) check
      i += 1
      continue 
    if s[j] not in letters: 
      j -= 1
      continue
    if s[i].lower() != s[j].lower():
      return False
    else:
      print(s[i].lower())
      print(s[j].lower())
      i += 1
      j -= 1
    
  return True

isPalindrome("A man, a plan, a canal: Panama")

def isPalindromeClean(s):
  """
  :type s: str
  :rtype: bool
  """
  # Two pointers
  i, j = 0, len(s) - 1

  while i < j:
    # Skip non-alphanumeric characters
    while i < j and not s[i].isalnum():
        i += 1
    while i < j and not s[j].isalnum():
        j -= 1
    
    # Compare characters (case-insensitive)
    if s[i].lower() != s[j].lower():
        return False
    
    i += 1
    j -= 1

  return True

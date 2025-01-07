# Medium, Hash Map / Array Question
# DIDNT SOLVE. LOOKED AT SOLNS
'''
Encode and Decode Strings
Design an algorithm to encode a list of strings to a single string. The encoded string is then decoded back to the original list of strings.

Please implement encode and decode

Example 1:
Input: ["neet","code","love","you"]
Output:["neet","code","love","you"]

Example 2:
Input: ["we","say",":","yes"]
Output: ["we","say",":","yes"]

Constraints:

0 <= strs.length < 100
0 <= strs[i].length < 200
strs[i] contains only UTF-8 characters.
'''

'''
Problem: Encode and Decode Strings
Design an algorithm to encode a list of strings to a single string, and 
then decode that single string back to the original list of strings. 

You need to implement two functions:

encode(strs: List[str]) -> str: 
This function takes a list of strings as input and returns a single encoded string.

decode(s: str) -> List[str]: 
This function takes the encoded string as input and returns the original list of strings.

The encoding should be designed in such a way that the original list of 
strings can be accurately reconstructed from the encoded string.
'''

# Approach 1: Length Prefixing (Popular in Network Protocols)

# List[str] -> str
def encode(strs):
    """Encodes a list of strings into a single string."""
    # For each string, we add its length followed by '#' then the string
    return ''.join(f"{len(s)}#{s}" for s in strs)

def decode(s):
  """Decodes a single string to a list of strings."""
  result = []
  i = 0
  while i < len(s):
      # Find the '#' delimiter
      j = i
      while s[j] != '#':
          j += 1
      # Get length of next string
      length = int(s[i:j])
      # Extract the string and add to result
      result.append(s[j + 1:j + 1 + length])
      # Move pointer
      i = j + 1 + length
  return result

# str -> List[str]
def decode(s):
  """Decodes a single string to a list of strings."""
  result = []
  i = 0
  while i < len(s):
      # Find the '#' delimiter
      j = i
      while s[j] != '#':
          j += 1
      # Get length of next string
      length = int(s[i:j])
      # Extract the string and add to result
      result.append(s[j + 1:j + 1 + length])
      # Move pointer
      i = j + 1 + length
  return result


# 49, Medium, Hashmaps & Arrays
'''
Given an array of strings strs, group the 
anagrams together. You can return the answer in any order.
'''

# Anagram:
'''
An anagram is a word or phrase formed by rearranging the letters 
of a different word or phrase, using all the original letters exactly once.
'''

'''
Example 1:
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Explanation:

There is no string in strs that can be rearranged to form "bat".
The strings "nat" and "tan" are anagrams as they can be rearranged to form each other.
The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other.

Example 2:
Input: strs = [""]
Output: [[""]]

Example 3:
Input: strs = ["a"]
Output: [["a"]]
'''

# brainstorm / idea:
# have to look at each char in each word
# iterate through the list

# Hint from gpt:
'''
Hint for the Solution
Use a dictionary to group words with the same sorted form together.

The key in the dictionary can be the sorted version of each string.
The value is a list of words that share the same sorted form.
Iterate through each word in the input array:

Sort the characters of the word to generate its "signature."
Use the signature as a key in the dictionary and append the word to the corresponding value.
Finally, collect all the values from the dictionary to get the grouped anagrams.
'''

# Good solution, O(n * k log k), where n is # of strings in input array, k is max length of any string, k log k is from sorting each string
# Space complexity: O(n * k) to store all strings in the hashmap
def groupAnagrams(strs):
  ret = []
  visited = {}
  for i in range(len(strs)):
      str_key = "".join(sorted(strs[i])) # O(k log k) for string
      if str_key in visited: # O(1) check
          visited[str_key].append(strs[i]) # O(1) add
      else:
          visited[str_key] = [strs[i]] # O(1) add

  # O(n)
  for item in visited.values(): # .key, .values, .items
      ret.append(item)

  return ret
    
      
          
  

# can't think of solution: here's shit brute force O(n^2) solution (probably even worse):
# didn't even write this:
def groupAnagramsBad(strs):
    """
    :type strs: List[str]
    :rtype: List[List[str]]
    """
    ret = []
    visited = [False] * len(strs)  # Track visited strings to avoid duplication
    
    for i in range(len(strs)):
        if visited[i]:
            continue
        
        current_group = [strs[i]]  # Start a new group
        visited[i] = True
        
        for j in range(i + 1, len(strs)):
            if visited[j]:
                continue
            
            # Check if two strings are anagrams by comparing sorted versions
            if set(strs[i]) == set(strs[j]) and sorted(strs[i]) == sorted(strs[j]):
                current_group.append(strs[j])
                visited[j] = True
        
        ret.append(current_group)
    
    return ret


# 10 -> i = 9 -> goes to 8


print(set("aasdf"))
a = "".join(sorted("lkfjgfv")) # separator.join(iterable), sorted is O(n log n), join is O(n), so total is O(n log n)
# separator in this case is nothing, and it separates each item in the iterable to make it a string
print(a)

strs = ["nozzle","punjabi","waterlogged","imprison","crux","numismatists","sultans","rambles","deprecating"]
for i in range(len(strs)):
    str_key = "".join(sorted(strs[i])) # O(n log n) for string
    print(str_key)
    # print("2: ", strs[i].sort()) doesn't work!
    # .sort() sorts in place
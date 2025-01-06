# Custom Question:
# (Traced), Used to Learn

def lengthOfLongestSubstring(s):
    char_set = set()  # To track unique characters
    left = 0
    max_length = 0
    
    for right in range(len(s)):
        while s[right] in char_set:  # Shrink the window if a duplicate is found
            char_set.remove(s[left])
            left += 1
        char_set.add(s[right])  # Add the new character to the window
        max_length = max(max_length, right - left + 1)
    
    return max_length

# Example:
print(lengthOfLongestSubstring("abcb"))  # Output: 3 (substring "abc")

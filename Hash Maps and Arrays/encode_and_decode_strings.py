# COMPLETED
"""
Encode and Decode Strings - Comprehensive Solutions

The goal is to design an algorithm to encode a list of strings into a single string
and decode it back into the original list of strings. The encoding and decoding
must handle edge cases like empty strings, special characters (e.g., "#"), and strings
with numbers.

This file includes:
1. A naive solution using a non-ASCII delimiter.
2. The optimal solution using length-prefixing and a delimiter.
3. An improved solution that escapes the delimiter.
"""

'''
DELIMITER:
A delimiter is a character or sequence of characters used to mark 
boundaries between different parts of data in a string. Delimiters 
are widely used in text processing to separate values, fields, or elements.
'''

# --- Naive Solution: Using a Non-ASCII Delimiter ---

def encode_naive(strs):
    """
    Encodes a list of strings into a single string using a non-ASCII delimiter.
    """
    # Use a character unlikely to appear in the strings (e.g., 'þ')
    delimiter = 'þ'
    return delimiter.join(strs)

def decode_naive(s):
    """
    Decodes a single string back into a list of strings using the naive approach.
    """
    delimiter = 'þ'
    return s.split(delimiter) # remember this syntax

# Explanation:
# - This works as long as the chosen delimiter (e.g., 'þ') does not appear in the strings.
# - If the delimiter exists in the original strings, decoding will fail.

# Example:
# Input: ["hello", "world"]
# Encoded: "helloþworld"
# Decoded: ["hello", "world"]

# Pros:
# - Simple and easy to implement.
# Cons:
# - Not robust if strings contain the delimiter.

# --- Optimal Solution: Length Prefixing with a Delimiter ---

# coded this by self!
# return "".join(f"{len(s)}#{s}" for s in strs)
def encode_length_prefix(strs):
    """
    Encodes a list of strings into a single string using length-prefixing.
    Each string is encoded as: <length>#<string>.
    """
    # Use '#' as the delimiter between the length and the string

    # return ''.join(f"{len(s)}#{s}" for s in strs)
    return "".join(f"{len(s)}#{s}" for s in strs) # works because join takes an iterable
# '3#abc   4#abcd'

# use two pointer
def decode_length_prefix(s):
    l = 0
    r = l
    ret = []
    while l < len(s):
        while s[r] != '#':
            r += 1
        str_length = int(s[l:r])
        ret.append(s[r+1:r+1+str_length]) # slicing goes to second param - 1 index
        l = r + 1 + str_length
        r = l
    return ret

strs = ["hello", "world"]
a = encode_length_prefix(strs) #a is a string
print(a)
b = decode_length_prefix(a) # b is a list
print(b)

# AI SOLUTION ALTERNATIVE TO ABOVE:
'''
def decode_length_prefix(s):
    """
    Decodes a single string back into a list of strings using length-prefixing.
    """
    result = []
    i = 0
    while i < len(s):
        # Find the '#' delimiter to separate the length from the string
        j = i
        while s[j] != '#':
            j += 1
        # Extract the length of the next string
        length = int(s[i:j])
        # Extract the string of the given length
        result.append(s[j + 1:j + 1 + length])
        # Move the pointer to the next encoded segment
        i = j + 1 + length
    return result
'''

# Explanation:
# - This solution is robust because the length prefix tells the decoder
#   exactly how many characters to read for each string.
# - The '#' delimiter separates the length from the string itself, ensuring no ambiguity.

# Example:
# Input: ["hello", "world"]
# Encoded: "5#hello5#world"
# Decoded: ["hello", "world"]

# Pros:
# - Handles all edge cases, including empty strings and strings with numbers or '#'.
# - Efficient and widely used in real-world systems.
# Cons:
# - Requires explicit handling of the delimiter during encoding/decoding.

# --- Improved Solution: Escaping the Delimiter ---

def encode_escape_delimiter(strs):
    """
    Encodes a list of strings into a single string with escaping.
    Replaces '#' in the original strings with '##' to avoid conflicts with the delimiter.
    """
    return ''.join(f"{len(s.replace('#', '##'))}#{s.replace('#', '##')}" for s in strs)

def decode_escape_delimiter(s):
    """
    Decodes a single string back into a list of strings, handling escaped delimiters.
    """
    result = []
    i = 0
    while i < len(s):
        # Find the '#' delimiter to separate the length from the string
        j = i
        while s[j] != '#':
            j += 1
        # Extract the length of the next string
        length = int(s[i:j])
        # Extract the encoded string of the given length
        encoded_str = s[j + 1:j + 1 + length]
        # Unescape '##' back to '#'
        result.append(encoded_str.replace('##', '#'))
        # Move the pointer to the next encoded segment
        i = j + 1 + length
    return result

# Explanation:
# - Escaping ensures that any '#' characters in the original strings are safely encoded as '##'.
# - During decoding, '##' is replaced back with '#' to reconstruct the original strings.

# Example:
# Input: ["hello", "co#de", "#love#"]
# Encoded: "5#hello6#co##de7##love##"
# Decoded: ["hello", "co#de", "#love#"]

# Pros:
# - Fully robust against all edge cases, including strings containing '#'.
# - Widely applicable and error-proof.
# Cons:
# - Slightly more complex due to escaping and unescaping logic.

# --- Testing the Solutions ---

if __name__ == "__main__":
    # Test cases
    test_cases = [
        ["hello", "world"],      # Basic case
        ["", "abc", "123"],      # Empty string and numbers
        ["#", "##", "###"],      # Strings containing the delimiter
        ["hello", "co#de"],      # Strings with mixed content
        []                       # Empty list
    ]

    # Naive Solution
    print("Naive Solution:")
    for case in test_cases:
        encoded = encode_naive(case)
        decoded = decode_naive(encoded)
        print(f"Original: {case}, Encoded: {encoded}, Decoded: {decoded}")

    # Length Prefix Solution
    print("\nLength Prefix Solution:")
    for case in test_cases:
        encoded = encode_length_prefix(case)
        decoded = decode_length_prefix(encoded)
        print(f"Original: {case}, Encoded: {encoded}, Decoded: {decoded}")

    # Escaping Delimiter Solution
    print("\nEscaping Delimiter Solution:")
    for case in test_cases:
        encoded = encode_escape_delimiter(case)
        decoded = decode_escape_delimiter(encoded)
        print(f"Original: {case}, Encoded: {encoded}, Decoded: {decoded}")

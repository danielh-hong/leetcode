# 20. Valid Parentheses
# Easy Stack Problem

'''
Given a string s containing just the characters 
'(', ')', '{', '}', '[' and ']', determine if the 
input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 
Example 1:
Input: s = "()"
Output: true

Example 2:
Input: s = "()[]{}"
Output: true

Example 3:
Input: s = "(]"
Output: false

Example 4:
Input: s = "([])"
Output: true
'''

# Brainstorming Soln:
# Create dictionary with key as open bracket, & value as corresponding closing bracket
# Instantiate stack
# Iterate through the string, pushing any open bracket to the stack (stack with items being added to end of list)
# Ex: for (), ( would be in stack  
# Every time a closing bracket is reached, check if it is equal to the corresponding closing bracket of the next item in the stack by checking dictionary
# if not, return False
# If is, pop that item from the stack, continue iterating

# My O(n) solution:
def isValid(s):
    """
    :type s: str
    :rtype: bool
    """
    bracket_key = {"(": ")", "[": "]", "{": "}"}
    stack = []
    for i in range(len(s)):
        if s[i] in bracket_key: # O(1) and automatically checks for key (uses hashing to find key, too)
            stack.append(s[i]) # append adds to the end of the list            
        else: # (if it's a closing bracket)
            try: # Instead of try & except we could do: if not stack (which is if stack is empty)
                last_stack_item = stack.pop() # pop returns last item, and this is an open bracket (checking if it's empty)
            except:
                return False
            if s[i] != bracket_key[last_stack_item]:
                return False
            
    return True if len(stack) == 0 else False
                
s = "([])"
isValid(s)

# space analysis:
'''
def isValid(s):
    bracket_key = {"(": ")", "[": "]", "{": "}"}  # Constant space O(1)
    stack = []                                     # Variable space O(n)
    for i in range(len(s)):                       # Counter variable O(1)
        # ... rest of code

'''
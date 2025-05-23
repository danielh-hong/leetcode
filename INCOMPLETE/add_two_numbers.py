# 2. Add Two Numbers

'''
You are given two non-empty linked lists representing two non-negative integers. 
The digits are stored in reverse order, and each of their nodes contains a single digit. 
Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

 

Example 1:


Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
Example 2:

Input: l1 = [0], l2 = [0]
Output: [0]
Example 3:

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
'''
# Definition for singly-linked list.
class ListNode:
	def __init__(self, val=0, next=None):
		self.val = val  # The value stored in the node
		self.next = next  # Pointer to the next node in the list
            
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        carry = 0 # always reset to zero
        ret = ListNode() # keeps track of head
        cur = ret
        while l1 and l2:
              cur_sum = l1.val + l2.val
              cur.val = cur_sum % 10 + carry
              l1 = l1.next
              l2 = l2.next
              cur = cur.next
              carry = cur_sum // 10
              




        
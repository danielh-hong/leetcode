# Definition for singly-linked list.
class ListNode:
	def __init__(self, val=0, next=None):
		self.val = val  # The value stored in the node
		self.next = next  # Pointer to the next node in the list

# My soln:
def mergeTwoLists2(list1, list2):
	"""
	Merge two sorted linked lists into one sorted linked list.
	The merged list is created by splicing together the nodes of the two input lists.

	:param list1: ListNode - head of the first sorted linked list
	:param list2: ListNode - head of the second sorted linked list
	:return: ListNode - head of the merged sorted linked list
	"""
	ret = ListNode()  # ListNode itself is of the memory type of an address 
	cur = ret
	while list1 and list2:  # assuming last node's next is like "None" type
		if list1.val <= list2.val:
			cur.next = list1 # use cur.next since we don't want to rewrite value; we're just setting the pointer.
			cur = cur.next
			list1 = list1.next
		else:
			cur.next = list2
			cur = cur.next
			list2 = list2.next
		cur = cur.next

	if list2:
		cur.next = list2
	if list1:
		cur.next = list1
	return ret.next

# Given soln:
def mergeTwoLists(list1, list2):
	"""
	Merge two sorted linked lists into one sorted linked list.
	The merged list is created by splicing together the nodes of the two input lists.

	:param list1: ListNode - head of the first sorted linked list
	:param list2: ListNode - head of the second sorted linked list
	:return: ListNode - head of the merged sorted linked list
	"""
	# Step 1: Create a dummy node to start the merged list.
	dummy = ListNode()
	current = dummy  # 'current' will track the end of the merged list.

	# Step 2: Traverse both lists and attach the smaller node to 'current'.
	while list1 and list2:
		if list1.val <= list2.val:
			current.next = list1
			list1 = list1.next   # Move forward in list1
		else:
			current.next = list2
			list2 = list2.next   # Move forward in list2
		current = current.next   # Move current to the newly attached node

	# Step 3: Attach any remaining nodes from list1 or list2.
	if list1:
		current.next = list1
	elif list2:
		current.next = list2

	# Step 4: Return the merged list, starting after the dummy node.
	return dummy.next

# Linked List Implementation

class Node:
    """Node class for Linked List."""
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    """Linked List implementation."""
    def __init__(self):
        self.head = None

    def append(self, value):
        """Add a node at the end."""
        new_node = Node(value)
        if not self.head: # equivalent to if self.head is None
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def print_list(self):
        """Print all elements in the list."""
        current = self.head
        while current:
            print(current.value, end=" -> ")
            current = current.next
        print("None")

    def delete_node(self, value):
        """Delete the first node with value."""
        if not self.head:
            return
        if self.head.value == value:
            self.head = self.head.next
            return
        current = self.head
        while current.next and current.next.value != value:
            current = current.next
        if current.next:
            current.next = current.next.next

    def find(self, value):
        """Search for a node with given value."""
        current = self.head
        while current:
            if current.value == value:
                return True
            current = current.next
        return False


# Easy: Reverse Linked List

def reverse_linked_list(head):
    """
    Reverse a linked list.
    Args:
    head (Node): Head of the list.
    Returns:
    Node: New head of the reversed list.
    """
    prev = None
    current = head
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    return prev

# Example Usage:
ll = LinkedList()
for value in [1, 2, 3, 4, 5]:
    ll.append(value)
print("Original list:")
ll.print_list()
ll.head = reverse_linked_list(ll.head)
print("Reversed list:")
ll.print_list()


# Medium: Detect Cycle in Linked List

def has_cycle(head):
    """
    Detect cycle in a linked list.
    Args:
    head (Node): Head of the list.
    Returns:
    bool: True if cycle exists, else False.
    """
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False

# Example Usage:
ll = LinkedList()
for value in [1, 2, 3, 4]:
    ll.append(value)
cycle_node = ll.head.next.next
ll.head.next.next.next.next = cycle_node
print("Cycle detected:", has_cycle(ll.head))  # Output: True



# Hard: Find Intersection of Linked Lists

def find_intersection(headA, headB):
    """
    Find intersection node of two lists.
    Args:
    headA (Node): Head of first list.
    headB (Node): Head of second list.
    Returns:
    Node: Intersection node or None.
    """
    if not headA or not headB:
        return None
    a, b = headA, headB
    while a != b:
        a = a.next if a else headB
        b = b.next if b else headA
    return a

# Example Usage:
ll1 = LinkedList()
ll2 = LinkedList()
for value in [1, 2, 3]:
    ll1.append(value)
for value in [4, 5]:
    ll2.append(value)
intersection = Node(6)
ll1.head.next.next.next = intersection
ll2.head.next.next = intersection
intersection.next = Node(7)
intersection.next.next = Node(8)
print("Intersection node value:",
      find_intersection(ll1.head, ll2.head).value)  # Output: 6

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def print_list(self):
        curr = self
        while curr is not None:
            print(curr.val)
            curr = curr.next


# Basic reverse of a linked list
def reverse(head: Optional[ListNode]) -> Optional[ListNode]:
    prev = None
    curr = head
    while curr is not None:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node
    return prev

# Initialize a linked list of 10 elements with the head pointer called head
head = ListNode(1)
current = head
for i in range(2, 11):
    current.next = ListNode(i)
    current = current.next

#node1.print_list()
#rev = reverse(head)
#rev.print_list()

"""
Leetcode 92. Reverse Linked List II
Given the head of a singly linked list and two integers left and right 
where left <= right, reverse the nodes of the list from position left 
to position right, and return the reversed list.
"""

def reverseBetween(head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
    if not head or left == right:
        return head

    dummy = ListNode(0)
    dummy.next = head
    prev = dummy

    for _ in range(left - 1):
        prev = prev.next

    curr = prev.next
    for _ in range(right - left):
        temp = curr.next
        curr.next = temp.next
        temp.next = prev.next
        prev.next = temp

    return dummy.next

rev = reverseBetween(head, 2, 8)
head.print_list()
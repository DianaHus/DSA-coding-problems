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
rev = reverse(head)
rev.print_list()
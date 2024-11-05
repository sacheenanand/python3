'''
You are given the head of a linked list. Delete the middle node, and return the head of the modified linked list.

The middle node of a linked list of size n is the ⌊n / 2⌋th node from the start using 0-based indexing, where ⌊x⌋ denotes the largest integer less than or equal to x.

For n = 1, 2, 3, 4, and 5, the middle nodes are 0, 1, 1, 2, and 2, respectively.

delete the middle node of a linked list.

'''


def deletenode(self, head):
    if head.next is None:
        return None
    slow=fast=head
    prev = None
    while fast and fast.next:
        prev = slow
        fast = fast.next.next
        slow = slow.next
    prev.next = prev.next.next
    return head

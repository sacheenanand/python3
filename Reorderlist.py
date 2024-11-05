'''
You are given the head of a singly linked-list. The list can be represented as:

L0 → L1 → … → Ln - 1 → Ln
Reorder the list to be on the following form:

L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
You may not modify the values in the list's nodes. Only nodes themselves may be changed.

 

Example 1:

https://www.youtube.com/watch?v=R0Jl1R99ia4
'''
def reoderlist(self, head: Optional[ListNode]):
    if not head.next or not head.next.next:
        return 
    # split
    mid = end = head
    while end.next and end.next.next:
        end = end.next.next
        mid = mid.next
    p2 = mid.next
    mid.next = None
    # reverse linkedlist
    
    prev = None
    while p2 and p2.next:
        p2next = p2.next
        p2.next = None
        prev = p2
        p2 = p2.next
    p2.next = prev

    # merge
    p1 = head
    while p1 and p2:
        p1next = p1.next
        p2next = p2.next
        p1.next = p2
        p2.next = p1next
        p1 = p1next
        p2 = p2next















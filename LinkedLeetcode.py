# reverse a linked list

"""
1 -> 2 -> 3


"""

class Solution:
    def reverseList(self, head):
        prev = None
        curr = head

        while curr != None:

            next_p = curr.next
            curr.next = prev
            #reset
            prev = curr
            curr = next_p

        return prev
    
# reverse a linked list in recursive order
    

    
    

        
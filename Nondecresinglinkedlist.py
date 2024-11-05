class Node:
    def __init__(self, data, next=None):
        self.data=data
        self.next=next

    def insertNode(head, val):
        new_node = Node(val)
        if not head or val < head.data:
            new_node.next = head
            head = new_node
            return head
        
        cur = head
        while cur.next and cur.next.data < val:
            cur = cur.next
        new_node.next = cur.next
        cur.next = new_node
        return head
    

    
    

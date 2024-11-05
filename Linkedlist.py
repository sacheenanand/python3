class Node:
    def __init__(self, data, next=None):
        self.data=data
        self.next=next
def lengthoflinked(node):
    count = 0
    temp = node
    while temp is not None:
        count += 1
        temp=temp.next
    return count


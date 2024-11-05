'''
Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree.
'''


#recursive method
def kthSmallest(self,root:Optional[TreeNode], k:int):
    self.k = k
    self.result = None

    def inOder(root):
        if root is None or self.result is not None:
            return 
        inOrder(root.left)
        self.k -=1
        if self.k == 0:
            self.result = root.val
            return
        inOrder(root.right)

    inOrder(root)
    return self.result







        
        



